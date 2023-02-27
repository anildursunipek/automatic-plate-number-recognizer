import keras_ocr
import numpy as np
import pytesseract

class PlateReader:
    def __init__(self):
        self.pipeline = keras_ocr.pipeline.Pipeline()
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    def read_keras_ocr(self, plateFrame ,text):
        result = self.pipeline.recognize([plateFrame])
        temp_arr = []
        for idx in result[0]:
            temp_arr.append(idx[1][0][0])
            text = ""
        for idx in range(len(temp_arr)):
            text += f"{result[0][temp_arr.index(np.min(temp_arr))][0]}"
            temp_arr[temp_arr.index(np.min(temp_arr))] += 50000
        return text

    def read_tesseract(self, plateFrame, text):
        text = pytesseract.image_to_string(plateFrame, lang ='eng', config = '-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6 --oem 3')
        return text
