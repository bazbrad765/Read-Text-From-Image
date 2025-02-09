import pytesseract
import sys
from PIL import Image
from PIL import ImageEnhance                    
opsys = sys.platform
if opsys == "linux" or opsys == "linux2":
    try:
        pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
    except:
        pass
elif opsys == "win32":
    try:
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    except:
        pass
elif opsys == "darwin":
    try:
        pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"
    except:
        pass
else:
    print("Cannot find teseract ocr install - **please install to default location and try again**")

#gets picture and extract text
img_file = "toyota_inv.png"
img = Image.open(img_file)


sharpener = ImageEnhance.Sharpness(img)
for i in range(1):
    sharpener.enhance(2.0).show()
    img.save("newpic.png")



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
