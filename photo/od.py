import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def classification(img_name):
    image_path = "media\\" + str(img_name) # 여기에는 테스트할 이미지의 경로 및 이름을 넣어주시면 됩니다. 
    im = cv2.imread(image_path) # 이미지 읽기


    # object detection (물체 검출)
    bbox, label, conf = cv.detect_common_objects(im)

    return bbox, label, conf