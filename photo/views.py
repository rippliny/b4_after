from django.shortcuts import render, redirect
from PIL import Image
from PIL.ExifTags import TAGS
from .models import PhotoModel, CategoryModel
from .forms import ImageUpload
from .category import get_category

def fileUpload(request):
    if request.method == 'POST':
        photo = PhotoModel()
        user = request.user

        photo.user = user
        photo.imgfile = request.FILES["imgfile"]
        photo.save()
        
        upload_image = PhotoModel.objects.filter().last()
        get_category(upload_image)
        print(upload_image)
        
        category = CategoryModel()

        category.save()
        
        return redirect('/upload')
    
    else:
        imageupload = ImageUpload
        context = {
            'imageupload': imageupload,
        }
        return render(request, 'upload.html', context)


def main_cateory(request):
    if request.method == 'GET':
        category_name = CategoryModel.objects.get(category_name=category_name)
        
        return render(request, 'base.html', {'category_name':category_name})


def get_photo_info() :
        image = Image.open(" ") #이미지 파일 경로 또는 주소 입력
        info = image._getexif()
        image.close()

        taglabel = {}

        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            taglabel[decoded] = value

        print(taglabel['DateTimeOriginal'])  # 촬영 시각
        print(taglabel['Make'], taglabel['Model'])  # 카메라 기종

        # 촬영 위치
        exifGPS = taglabel['GPSInfo']
        latData = exifGPS[2]  # 위도(latitude)만 불러오기
        lonData = exifGPS[4]  # 경도(longitude)만 불러오기

        # 도(Degree), 분(Minute), 초(Second) 계산
        latDeg = latData[0]
        latMin = latData[1]
        latSec = latData[2]

        lonDeg = lonData[0]
        lonMin = lonData[1]
        lonSec = lonData[2]

        # 도, 분, 초로 나타내기
        Lat = str(int(latDeg)) + "°" + str(int(latMin)) + "'" + str(latSec) + "\"" + exifGPS[1]
        Lon = str(int(lonDeg)) + "°" + str(int(lonMin)) + "'" + str(lonSec) + "\"" + exifGPS[3]

        print(Lat, Lon)

        # 도 decimal로 나타내기
        # 위도 계산
        Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
        # 북위, 남위인지를 판단, 남위일 경우 -로 변경
        if exifGPS[1] == 'S': Lat = Lat * -1

        # 경도 계산
        Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
        # 동경, 서경인지를 판단, 서경일 경우 -로 변경
        if exifGPS[3] == 'W': Lon = Lon * -1

        print(Lat, ",", Lon)

def bookmark(request):
    photo_id = request.data.get('photo_id', None)
    bookmark_text = request.data.get('bookmark_text', True)
    
    if bookmark_text == 'bookmark_border':
        is_marked = True
    else:
        is_marked = False
        
    email = request.session.get('email', None)
    bookmark = Bookmark.objects.filter(photo_id=photo_id, email=email).first()
    
    if bookmark:
        bookmark.is_marked = is_marked
        bookmark.save()
    else:
        Bookmark.objects.create(photo_id=photo_id, is_marked=is_marked, email=email)
    return

def trash(request):
    photo_id = request.data.get('photo_id', None)
    trash_text = request.data.get('trash_text', True)

    if trash_text == 'trash_border':
        is_marked = True
    else:
        is_marked = False
        
    email = request.session.get('email', None)
    trash = Trash.objects.filter(photo_id=photo_id, email=email).first()
    
    if trash:
        trash.is_marked = is_marked
        trash.save()
    else:
        Trash.objects.create(photo_id=photo_id, is_marked=is_marked, email=email)
    return 