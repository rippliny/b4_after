from django.shortcuts import render, redirect
from PIL import Image
from PIL.ExifTags import TAGS
from .models import PhotoModel
from .forms import ImageUpload
from .od import classification
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def upload(request):
    if request.method == 'POST':
        photo = PhotoModel()
        user = request.user
        photo.user = user
        photo.img = request.FILES["img"]
        photo.category = classification(photo.img)[1]
        
        photo.save()
    
        return redirect('/upload')

    else:
        imageupload = ImageUpload
        context = {
            'imageupload': imageupload,
        }
        return render(request, 'upload.html', context)

def get_photo_info(request, id):
    if request.method == 'POST':
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

    if request.method == 'GET':
        return render(request, 'img_info.html')
    
# 즐겨찾기
@login_required
def favorites(request):
    photo_id = request.data.get('photo_id', None)
    favorites_text = request.data.get('favorites_text', False)
    
    if favorites_text == 'star_border':
        favorit = True
        
    else:
        favorit = False
        
    email = request.session.get('email', None)
    favorites = PhotoModel.objects.filter(photo_id=photo_id, email=email).first()
    
    if favorites:
        favorites.favorites = favorit
        favorites.save()
        
    else:
        PhotoModel.objects.create(photo_id=photo_id, favorit=favorit, email=email)
        
    return redirect('favorit/')
