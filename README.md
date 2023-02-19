# automatic-plate-number-recognizer
-----------------------------------------
Steps
-----
- Yeni python env oluşturuldu
- Yolov5 modeli implement edildi
- Yolov5 requirements.txt içerisindeki kütüphaneler pip ile mevcut python ortamına yüklendi
- plateFinder.py içerisinde PlateFinder class'ı oluşturuldu ve threading kütüphanesi içerisinden threading.Thread class'ı miras bırakılarak yeni bir class oluşturuldu.
- PlateFinder class'ının içerisinde startDetection ve detection method'ları eklendi.


Github Links
------------
- Yolov5 github -> https://github.com/ultralytics/yolov5
- yolov5 training notebook(google colab) -> https://colab.research.google.com/github/roboflow-ai/yolov5-custom-training-tutorial/blob/main/yolov5-custom-training.ipynb#scrollTo=X7yAi9hd-T4B

Plate Dataset
-------------
Kaggle -> https://www.kaggle.com/datasets/andrewmvd/car-plate-detection?select=images
Roboflow -> https://universe.roboflow.com/school-0bhfs/plate-number-recognition-dcqwk/dataset/1
