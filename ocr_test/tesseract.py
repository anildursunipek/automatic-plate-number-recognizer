import cv2
import pytesseract

img = cv2.imread("test_images/2023-02-27-14-42-45-0.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
predicted_result = pytesseract.image_to_string(gray, lang ='eng', config = '-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6 --oem 3')

print(predicted_result)
cv2.imshow("tses",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

