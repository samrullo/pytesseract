import os
from PIL import Image
import pytesseract

images_folder=r"C:\Users\amrul\Downloads\Telegram Desktop\ChatExport_2022-02-10\photos"
img_file="photo_647@10-02-2022_00-01-12_thumb.jpg"

text=pytesseract.image_to_string(Image.open(os.path.join(images_folder,img_file)),lang="jpn")
print(text)