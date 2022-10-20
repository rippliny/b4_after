from django.shortcuts import render, redirect
from PIL import Image
from PIL.ExifTags import TAGS

from user.models import UserModel
from .models import PhotoModel, Trash, Favorit
from .forms import ImageUpload
from .od import classification
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def category(request):
    return render(request, 'category.html')


@login_required
def fileUpload(request):
    if request.method == 'POST':
        photo = PhotoModel()
        user = request.user

        photo.user = user
        photo.img = request.FILES["img"]
        photo.save()
        photo.category = classification(photo.img)[1]
        photo.save()
    
        return redirect('/')

    else:
        imageupload = ImageUpload
        context = {
            'imageupload': imageupload,
        }
        return render(request, 'upload.html', context)


@login_required
def img_info(request, id):
    if request.method == 'GET':
        photo = PhotoModel.objects.get(id=id)
        image = PhotoModel.objects.all()
        context = {
            'photo': photo,
            'img': image,
            'id' : id,
        }
        return render(request, 'img_info.html', context)

    elif request.method == 'POST':
        photo = PhotoModel.objects.get(id=id)
        trash = Trash()
        trash.user = request.user
        trash.trash = photo.img
        trash.save()
        
        photo.delete()
      
        return redirect('/')


@login_required
def trash(request):
    user = request.user.is_authenticated
    trash = Trash.objects.all()
    if user:
        return render(request, 'trash.html', {'trash' : trash})
    else:
        return redirect('/sign-in')

# 즐겨찾기
@login_required
def favorit(request, id):
    if request.method == 'POST':
        photo = PhotoModel.objects.get(id=id)
        favorit = Favorit()
        favorit.user = request.user
        favorit.favorit = photo.img
        favorit.save()
            
        photo.delete()
      
        return redirect('/')

# 즐겨찾기 페이지
@login_required
def favorit_view(request):
    user = request.user.is_authenticated
    favorit = Favorit.objects.all()
    if user:
        return render(request, 'favorites.html', {'favorit' : favorit})
    else:
        return redirect('/sign-in')


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

        context = {
            'DateTime': DateTime,
            'ExifImageHeight': ExifImageHeight,
            'ExifImageWidth': ExifImageWidth,
            'ShutterSpeedValue': ShutterSpeedValue,
            'FNumber': FNumber,
            'Make': Make,
            'Model': Model,
            'LensModel': LensModel,
            'Lat' : Lat,
            'Lon' : Lon,
        }

        return render(request, img_info.html, context)


# # 즐겨찾기
# @login_required
# def favorites(request, id):
#     me = request.user
#     click_user = PhotoModel.objects.get(id=id)
#     if me in click_user.favorites.all():
#         click_user.favorites.remove(request.user)
#     else:
#         click_user.favorites.add(request.user)
#     return redirect('/')

# # 즐겨찾기 페이지
# @login_required
# def favorites_view(request):
#     me = request.user
#     photo = PhotoModel.objects.all().first()
#     favorit_list = photo.favorites.all()
#     favorit = photo.favorites.filter(username=me)
    
#     if me:
#         return render(request, 'favorites.html', {'photo':photo, 'favorit_list':favorit_list, 'favorit':favorit})
#     else:
#         return redirect('/')
