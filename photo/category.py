from django.shortcuts import render
import torch
import cv2
# from .models import PhotoModel
# import os
# from django.conf import settings
# settings.configure()

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
# img_folder = os.path.join(settings.MEDIA_URL)

def get_category(img):
    print(img)
    imgs = cv2.imread(img)

    results = model(imgs)

    result1 = results.xyxy[0], results.xyxy[0][0][0].item()
    result2 = results.pandas().xyxy[0]
    result3 = results.pandas().xyxy[0].to_numpy()
    
    return result2
