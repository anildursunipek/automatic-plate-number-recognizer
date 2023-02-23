# automatic-plate-number-recognizer
-----------------------------------
Setup
-----
- pip install -qr requirements.txt 
- Tensorflow gpu kurulumu
- keras-ocr kurulumu
- Keras için tensorflow=>2 ve üstü sürümler kullanılabilir

Steps
-----
- Yeni python env oluşturuldu
- Yolov5 modeli implement edildi
- Yolov5 requirements.txt içerisindeki kütüphaneler pip ile mevcut python ortamına yüklendi
- pip install -qr requirements.txt 
- plateFinder.py içerisinde PlateFinder class'ı oluşturuldu ve threading kütüphanesi içerisinden threading.Thread class'ı miras bırakılarak yeni bir class oluşturuldu.
- PlateFinder class'ının içerisinde startDetection ve detection method'ları eklendi.
- Torch'un cpu ile çalıştığı tespit edildi. Torch, torchvision ve torchaudio kaldırıldı ve pytorch'un sitesinden tekrar pip ile kurulumu yapıldı. Gpu çalışması aktif edildi.
- save_plate ve take_snapshot metodları eklendi. Threading kullanılarak tespit edilen plate'lerin her 3 saniyede bir detection klasörüne kayıt edilmesi sağlandı. Threading.Timer methodu kullanıldı.
- Görselden text çıkarmak için alternatiflere bakıldı. Görüntü işleme ile her bir karakter için tespit yapılabilir. Ek olarak paddleocr yada openalpr gibi kaynaklardan yararlanılarak yüksek accuracy çıkarılabilir.

Github Links
------------
- Yolov5 github -> https://github.com/ultralytics/yolov5
- yolov5 training notebook(google colab) -> https://colab.research.google.com/github/roboflow-ai/yolov5-custom-training-tutorial/blob/main/yolov5-custom-training.ipynb#scrollTo=X7yAi9hd-T4B
- Openalpr için github linkleri -> https://github.com/openalpr/openalpr |  https://github.com/peters/openalpr-windows 

Plate Dataset
-------------
- Kaggle -> https://www.kaggle.com/datasets/andrewmvd/car-plate-detection?select=images
- Roboflow -> https://universe.roboflow.com/school-0bhfs/plate-number-recognition-dcqwk/dataset/1

General Links
-------------
- Torch gpu kurulum linki(mevcut kullanılan sürüm cuda 11.6) -> https://pytorch.org/get-started/locally/ 

Helpful Links
-------------
- https://www.youtube.com/watch?v=6xklN4iiA0Q&ab_channel=Edgecate -> Plakaların belirli sürelerde nasıl kayıt edileceği ve open alpr gibi faydalı içeriklerin bulunduğu video.
- https://www.youtube.com/watch?v=BpXlQwcx67s&ab_channel=coderzero
- https://www.youtube.com/watch?v=i_30im3FlCs&ab_channel=TechieCoder
- https://www.youtube.com/watch?v=oyqNdcbKhew&ab_channel=RobMulla -> tesseract, easyocr ve keras_ocr karşılaştırması 
- https://www.educba.com/keras-ocr/ -> keras_ocr 
- https://medium.com/mlearning-ai/tesseract-vs-keras-ocr-vs-easyocr-ec8500b9455b -> keras_ocr, easyocr ve tesseract arasındaki karşılaştırma için başka bir bağlantı