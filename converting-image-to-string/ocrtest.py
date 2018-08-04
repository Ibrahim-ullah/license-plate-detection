import cv2
import pytesseract
from PIL import Image
print pytesseract.image_to_string(Image.open('pic.png'))

#to run the code you have to go to the terminal and type tesseract pic.png out.Here pic.png is the name of your picture and out indicates the 
#text file name where you are gonna save the string.
