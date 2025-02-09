import pytesseract
import sys
from PIL import Image  

opsys = sys.platform
print(opsys)

if opsys == "linux":
    try:
        pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
    except:
        pass



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
