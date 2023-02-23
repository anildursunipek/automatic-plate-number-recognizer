import threading
import torch
import cv2
import numpy as np
from datetime import datetime
import time
import keras_ocr

class PlateFinder(threading.Thread):  
  """
  This class
  """
  def __init__(self, threadName: str, video_source, video_out = None):
    threading.Thread.__init__(self) 
    self.video_source = video_source
    self.threadName = threadName
    self.video_out = video_out
    print("[INFO] Loading Model. . .")
    self.model = self.load_model(yolov5Path= "yolov5", customWeightsPath= "yolov5/best.pt")
    self.model.conf = 0.50 # NMS confidence threshold
    self.model.iou = 0.50 # NMS IoU threshold
    threading.Timer(15.0, self.take_snapshot).start()
    self.pipeline = keras_ocr.pipeline.Pipeline()
    
  def run(self):
    """
    """
    self.start_detection()

  def load_model(self, yolov5Path, customWeightsPath):
    """
    This function loads the yolov5 model.

    Parameters:
      yolov5Path(string) = Path of the yolov5 files.
      customWeightPath(string) = Path of custom weights adress 
    
    Returns:
      A pytorch model which is loading custom weights.
    """
    return torch.hub.load(repo_or_dir= yolov5Path, model= 'custom', source= 'local', path= customWeightsPath, force_reload= True)

  def start_detection(self):
    """
    Function description
    
    Parameters:
      video_source(int):
      video_out(string):
    
    Returns(void)
    """
    global frame
    global labels
    global cordinates
    if torch.cuda.is_available():
      device = torch.device(0)
      self.model.to(device)

    cap = cv2.VideoCapture(self.video_source)

    # Writing to a video
    # Convert the default resolutions from float to integer.
    self.frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    self.frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    self.framerate = int(cap.get(cv2.CAP_PROP_FPS)) # or 30,20,10 ...
    
    if self.video_out is not None: 
      codec = cv2.VideoWriter_fourcc(*'mp4v')
      resolution = (self.frame_width, self.frame_height)
      frame_Output = cv2.VideoWriter(self.video_out, codec, self.framerate, resolution)

    while cap.isOpened():
      succes, frame = cap.read()
      if succes:
        cv2_im = frame
        resultFrame, labels, cordinates = self.detection(cv2_im, self.model)
        #self.save_plate(frame, labels,cordinates, False)
          
        # Show Frame
        cv2.imshow('Video Out', np.squeeze(resultFrame.render()))

        if self.video_out is not None:
          print(f"[INFO] Saving output video. . .")
          frame_Output.write(resultFrame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
          print("[INFO] Camera Turns Off. . .")
          break
      else:
        print("[ERROR INFO] Failed to capture frame")
        break
    
    cap.release()
    cv2.destroyAllWindows()

  def save_plate(self, frame, labels, cordinates, take_photo):
    """
    Function description

    Parameters:
      labels:
      cordinates:
      take_photo:

    returns(void)
    """
    if take_photo and len(labels) != 0:
      for self.idx, plateIndex in enumerate(range(len(labels))):
        x_min, y_min, x_max, y_max = int(cordinates[plateIndex][0]), int(cordinates[plateIndex][1]), int(cordinates[plateIndex][2]), int(cordinates[plateIndex][3])
        plateFrame = frame[y_min+5:y_max+5, x_min+5:x_max+5]  

        if plateFrame.shape[0] > self.frame_height/15 and plateFrame.shape[1] > self.frame_width/12:
          self.now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
          obj_filename = f'''{self.now}-{self.idx}'''
          obj_path = f'''./detected/{obj_filename}.png'''
          #cv2.imwrite(f'''{obj_path}''', plateFrame)
          text = self.text_detection(plateFrame)
          self.save_to_database(text)

  def text_detection(self, plateFrame):
    result = self.pipeline.recognize([plateFrame])
    temp_arr = []
    for idx in result[0]:
      temp_arr.append(idx[1][0][0])
      text = ""
    for idx in range(len(temp_arr)):
      text += f"{result[0][temp_arr.index(np.min(temp_arr))][0]}"
      temp_arr[temp_arr.index(np.min(temp_arr))] += 50000
    return text

  def save_to_database(self, text):
    print(text)

  def take_snapshot(self):
    """
    Function description
    ...
    returns(void)
    """
    print("Take snapshot init")
    self.save_plate(frame, labels, cordinates, True)
    thread = threading.Timer(3.0, self.take_snapshot)
    thread.daemon = True
    thread.start()

  def detection(self, frame, model):
    """ 
    Function description
    ...
    Parameters:
      result:
      labels:
      cordinates:

    Returns:
      result:
      labels:
      cordinates:

    Example
    -------
    print(result.xyxyn[0])
    
    #      xmin    ymin    xmax   ymax  confidence  class    name
    # 0  749.50   43.50  1148.0  704.5    0.874023      0  person
    # 1  433.50  433.50   517.5  714.5    0.687988     27     tie
    # 2  114.75  195.75  1095.0  708.0    0.624512      0  person
    # 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
    """
    result = self.model(frame)
    labels, cordinates = result.xyxy[0][:,-1], result.xyxy[0][:,:-2]
    return result, labels, cordinates

if __name__ == '__main__':
  # Test Code
  thread = PlateFinder("Thread - 1",video_source=0,video_out=None)
  thread.start()
  thread.join()
