import pytesseract
from PIL import Image  



#exe path for pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#gets picture and extract text
img_file = "toyota_inv.png"
img = Image.open(img_file)
text = pytesseract.image_to_string(img)

#check for txt file, create it if needed and write text to it
try:
    file = open("extracted_text.txt", "x")
except:
    file = open("extracted_text.txt", "w")
file.write(text)
file.close()
print("Text extracted successfully! -- please open 'extracted_text.text' within this folder to view text.")
print("To view extracted text in colsole, hit '1' or hit anything else to close")
x = input("")
if x == str(1):
    print(text)
