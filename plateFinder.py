import threading
import torch
import cv2
import numpy as np

  
def startDetection(video_source = 0, video_out = None, ):
  """
  Function description
  
  Parameters:
    video_source(int):
    video_out(string):
  
  Returns(void)
  """
  print("[INFO] Loading Model. . .")
  model = loadModel(yolov5Path= "yolov5", customWeightsPath= "yolov5/best.pt")
  if torch.cuda.is_available():
    device = torch.device(0)
    model.to(device)

  model.conf = 0.45 # NMS confidence threshold
  model.iou = 0.5 # NMS IoU threshold
  #classes = self.model.names

  cap = cv2.VideoCapture(video_source)

  # Writing to a video
  # Default resolutions
  # Convert the default resolutions from float to integer.
  if video_out is not None: 
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    framerate = int(cap.get(cv2.CAP_PROP_FPS)) # or 30,20,10 ...
    resolution = (frame_width, frame_height)
    frame_Output = cv2.VideoWriter(video_out, codec, framerate, resolution)

  while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # Make Detection
        result, labels, cordinates = detection(frame, model)
        
        #if(len(labels) != 0):
            #image_to_text(frame, labels, cordinates)

        for i in range(len(labels)):
            x_min, y_min, x_max, y_max = int(cordinates[i][0]), int(cordinates[i][1]), int(cordinates[i][2]), int(cordinates[i][3])
            temp_frame = frame[y_min:y_max, x_min:x_max]
        
        # Show Frame
        cv2.imshow('Video Out', np.squeeze(result.render()))
        
        if video_out is not None:
            print(f"[INFO] Saving output video. . .")
            frame_Output.write(result)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("[INFO] Camera Turns Off. . .")
            break
    else:
        break
  
  cap.release()
  cv2.destroyAllWindows()

def loadModel(yolov5Path:str, customWeightsPath:str):
  """
  This function loads the yolov5 model.

  Parameters:
    yolov5Path(string): Path of the yolov5 files.
    customWeightPath(string): Path of custom weights adress 
  
  Returns:
    A pytorch model which is loading custom weights.
  """
  return torch.hub.load(repo_or_dir= yolov5Path, model= 'custom', source= 'local', path= customWeightsPath, force_reload= True)

def detection(frame, model):
  """ 
  Function description

  Parameters:
    frame(numpy.array):
    model(pytorch.model):
  returns:
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
  result = model(frame)
  labels, cordinates = result.xyxy[0][:,-1], result.xyxy[0][:,:-2]
  return result, labels, cordinates

class PlateFinder(threading.Thread):  
  """
  """
  def __init__(self, threadName: str, video_source):
    threading.Thread.__init__(self) 
    self.video_source = video_source
    self.video_out = None
    self.threadName = threadName
    self.frameCounter = 0

    print("[INFO] Loading Model. . .")
    self.model = self.loadModel(yolov5Path= "yolov5", customWeightsPath= "yolov5/best.pt")
    
  def run(self):
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
    return torch.hub.load(repo_or_dir= yolov5Path, model= 'custom', source= 'local', path= customWeightsPath, force_reload= True)
  
  def startDetection(self):
    """
    Function description
    
    Parameters:
      video_source(int):
      video_out(string):
    
    Returns(void)
    """
    if torch.cuda.is_available():
      device = torch.device(0)
      self.model.to(device)

    self.model.conf = 0.65 # NMS confidence threshold
    self.model.iou = 0.45 # NMS IoU threshold
    #classes = self.model.names

    cap = cv2.VideoCapture(self.video_source)

    # Writing to a video
    # Default resolutions
    # Convert the default resolutions from float to integer.
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    framerate = int(cap.get(cv2.CAP_PROP_FPS)) # or 30,20,10 ...
    if self.video_out is not None: 
      codec = cv2.VideoWriter_fourcc(*'mp4v')
      resolution = (frame_width, frame_height)
      frame_Output = cv2.VideoWriter(self.video_out, codec, framerate, resolution)

    while cap.isOpened():
      ret, frame = cap.read()
      if ret == True:
        # Make Detection
        result, labels, cordinates = self.detection(frame, self.model)
        
        if(len(labels) != 0):
          for i in range(len(labels)):
            x_min, y_min, x_max, y_max = int(cordinates[i][0]), int(cordinates[i][1]), int(cordinates[i][2]), int(cordinates[i][3])
            temp_frame = frame[y_min:y_max, x_min:x_max]
            print(temp_frame.size , "       ", temp_frame.shape)
            if temp_frame.shape[0] > frame_height/12 and temp_frame.shape[1] > frame_width/8:
              cv2.imwrite(f"rec/test{self.counter}.png", temp_frame)
          
        # Show Frame
        cv2.imshow('Video Out', np.squeeze(result.render()))
        
        if self.video_out is not None:
          print(f"[INFO] Saving output video. . .")
          frame_Output.write(result)

        if cv2.waitKey(10) & 0xFF == ord('q'):
          print("[INFO] Camera Turns Off. . .")
          break
      else:
        print("[ERROR INFO] Failed to capture frame")
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
    result = self.model(frame)
    labels, cordinates = result.xyxy[0][:,-1], result.xyxy[0][:,:-2]
    return result, labels, cordinates


if __name__ == '__main__':

  # Test Code
  thread = PlateFinder("Thread - 1", 0)
  thread.start()
  thread.join()

  # Test Code
  # thread_1 = threading.Thread(target= startDetection, args=(0,))
  # thread_1.start()
  # thread_1.join()




  