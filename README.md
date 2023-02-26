# automatic-plate-number-recognizer
-----------------------------------
Build
-----
- Creating new python env 
    * Windows
        * python -m venv env
        * .\env\Scripts\activate
    * Linux
        * python3 -m venv env
        * source env/bin/activate,
- pip install -r requirements.txt
- Torch Gpu Kurulumu: https://pytorch.org/get-started/locally/ 
     * Ex: pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

Used Models
-----------
* YOLOV5
* Keras_ocr

Dependencies
------------
* gitpython
* ipython 
* matplotlib>=3.2.2
* numpy>=1.18.5
* opencv-python>=4.1.1
* Pillow>=7.1.2
* psutil 
* PyYAML>=5.3.1
* requests>=2.23.0
* scipy>=1.4.1
* thop>=0.1.1 
* tqdm>=4.64.0
* pandas>=1.1.4
* seaborn>=0.11.0
* setuptools>=65.5.1
* wheel>=0.38.0
* keras-ocr
* tensorflow


Github Links
------------
- Yolov5 github -> https://github.com/ultralytics/yolov5
- https://github.com/ultralytics/yolov5/issues/36
- Openalpr için github linkleri -> https://github.com/openalpr/openalpr | https://github.com/peters/openalpr-windows 

Plate Dataset
-------------
- Kaggle -> https://www.kaggle.com/datasets/andrewmvd/car-plate-detection?select=images
- Roboflow -> https://universe.roboflow.com/school-0bhfs/plate-number-recognition-dcqwk/dataset/1

Helpful Links
-------------
- yolov5 training notebook(google colab) -> https://colab.research.google.com/github/roboflow-ai/yolov5-custom-training-tutorial/blob/main/yolov5-custom-training.ipynb#scrollTo=X7yAi9hd-T4B
- https://www.youtube.com/watch?v=6xklN4iiA0Q&ab_channel=Edgecate -> Plakaların belirli sürelerde nasıl kayıt edileceği ve open alpr gibi faydalı içeriklerin bulunduğu video.
- https://www.youtube.com/watch?v=BpXlQwcx67s&ab_channel=coderzero
- https://www.kaggle.com/code/aslanahmedov/automatic-number-plate-recognition#7.4-HTTP-METHOD-UPLOAD-FILE-IN-FLASK
- https://www.youtube.com/watch?v=i_30im3FlCs&ab_channel=TechieCoder
- https://www.youtube.com/watch?v=oyqNdcbKhew&ab_channel=RobMulla -> tesseract, easyocr ve keras_ocr karşılaştırması 
- https://www.educba.com/keras-ocr/ -> keras_ocr 
- https://medium.com/mlearning-ai/tesseract-vs-keras-ocr-vs-easyocr-ec8500b9455b -> keras_ocr, easyocr ve tesseract arasındaki karşılaştırma için başka bir bağlantı