import keras_ocr
import numpy as np

class PlateReader:
    def __init__(self):
        self.pipeline = keras_ocr.pipeline.Pipeline()

    def read(self, plateFrame):
        result = self.pipeline.recognize([plateFrame])
        temp_arr = []
        for idx in result[0]:
            temp_arr.append(idx[1][0][0])
            text = ""
        for idx in range(len(temp_arr)):
            text += f"{result[0][temp_arr.index(np.min(temp_arr))][0]}"
            temp_arr[temp_arr.index(np.min(temp_arr))] += 50000
        return text

