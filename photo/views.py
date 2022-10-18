from django.shortcuts import render
from PIL import Image
from pprint import pprint
from PIL.ExifTags import TAGS

# Create your views here.

def get_photo_info() :
    image = Image.open(" ")     # image input directory or url, etc.
    info = image._getexif();
    image.close()

    taglabel = {}

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        taglabel[decoded] = value

        print(taglabel)

        # print(taglabel['DateTimeOriginal']) #촬영 시각
        # print(taglabel['Make'], taglabel['Model']) # 카메라 기종
        # print(taglabel['GPSInfo']) #촬영 장소