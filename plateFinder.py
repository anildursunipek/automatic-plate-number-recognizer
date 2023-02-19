import threading
import time
import torch
import cv2
import numpy as np

class PlateFinder(threading.Thread):  
  """
  """
  def __init__(self, threadName: str):
    threading.Thread.__init__(self) 
    video_out = None
    self.threadName = threadName
    print("[INFO] Loading Model. . .")
    self.model = self.loadModel(yolov5Path= "yolov5", customWeightsPath= "yolovt/best.py")
    
  def run(self, video_source):
    """
    """
    self.startDetection()

  def loadModel(self, yolov5Path, customWeightsPath):
    """
    This function loads the yolov5 model.

    Parameters:
      yolov5Path(string) = Path of the yolov5 files.
      customWeightPath(string) = Path of custom weights adress 
    
    Returns:
      A pytorch model which is loading custom weights.
    """
    return torch.hub.load(yolov5Path, 'custom', source= 'local', path= customWeightsPath, force_reload=True)
  
  def startDetection(self):
    if torch.cuda.is_available():
      device = torch.device(0)
      self.model.to(device)

    self.model.conf = 0.45 # NMS confidence threshold
    self.model.iou = 0.5 # NMS IoU threshold
    #classes = self.model.names

    cap = cv2.VideoCapture(self.video_source)

    # Writing to a video
    # Default resolutions
    # Convert the default resolutions from float to integer.
    if self.video_out is not None: 
      frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
      frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
      codec = cv2.VideoWriter_fourcc(*'mp4v')
      framerate = int(cap.get(cv2.CAP_PROP_FPS)) # or 30,20,10 ...
      resolution = (frame_width, frame_height)
      frame_Output = cv2.VideoWriter(self.video_out, codec, framerate, resolution)

    while cap.isOpened():
      ret, frame = cap.read()
      if ret == True:
          # Make Detection
          result, labels, cordinates = self.detection(frame)
          
          #if(len(labels) != 0):
              #image_to_text(frame, labels, cordinates)

          for i in range(len(labels)):
              x_min, y_min, x_max, y_max = int(cordinates[i][0]), int(cordinates[i][1]), int(cordinates[i][2]), int(cordinates[i][3])
              temp_frame = frame[y_min:y_max, x_min:x_max]
          
          # Show Frame
          cv2.imshow('Video Out', np.squeeze(result.render()))
          
          if self.video_out is not None:
              print(f"[INFO] Saving output video. . .")
              frame_Output.write(result)

          if cv2.waitKey(10) & 0xFF == ord('q'):
              print("[INFO] Camera Turns Off. . .")
              break
      else:
          break
    
    cap.release()
    cv2.destroyAllWindows()

  def detection(self, frame, model):
    """ 
    Example
    -------
    print(result.xyxyn[0])
    
    #      xmin    ymin    xmax   ymax  confidence  class    name
    # 0  749.50   43.50  1148.0  704.5    0.874023      0  person
    # 1  433.50  433.50   517.5  714.5    0.687988     27     tie
    # 2  114.75  195.75  1095.0  708.0    0.624512      0  person
    # 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
    """
    result = model(frame)
    labels, cordinates = result.xyxy[0][:,-1], result.xyxy[0][:,:-2]
    return result, labels, cordinates


if __name__ == '__main__':
  thread = PlateFinder("Thread - 1")
  thread.start()
  thread.join()





  