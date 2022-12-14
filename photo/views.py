from django.shortcuts import render, redirect
from PIL import Image
from PIL.ExifTags import TAGS
from user.models import UserModel
from .models import Category, PhotoModel, Trash, Favorit, Category
from .forms import ImageUpload
from .od import classification
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def category(request):
    pht = PhotoModel.objects.all()
    ctg = Category.objects.all()
    return render(request, 'category.html', {'pht':pht, 'ctg':ctg})


@login_required
def fileUpload(request):
    if request.method == 'POST':
        photo = PhotoModel()
        user = request.user

        photo.user = user
        photo.img = request.FILES["img"]
        photo.save()

        categories = classification(photo.img)[1]
        # ctg.name = categories
        # ctg.save()
        
        # metadata = get_photo_info(photo.img)
        
        # print(metadata)
        
        categories = Category.objects.filter(name__in=categories)
        if categories:
            photo.categories.add(*categories)
        else:
            photo.categories.add(81)
            
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
        trash.trash_img = photo.img
        trash.save()
        
        photo.delete()
      
        return redirect('/')


@login_required
def trash(request):
    user = request.user.is_authenticated
    trash = Trash.objects.all()
    if user:
        return render(request, 'trash.html', {'trash_img' : trash})
    else:
        return redirect('/sign-in')


# ????????????
@login_required
def favorit(request, id):
    if request.method == 'POST':
        photo = PhotoModel.objects.get(id=id)
        favorit = Favorit()
        favorit.user = request.user
        favorit.favorit = photo.img
        favorit.save()
            
      
        return redirect('/')


# ???????????? ?????????
@login_required
def favorit_view(request):
    user = request.user.is_authenticated
    favorit = Favorit.objects.all()
    if user:
        return render(request, 'favorites.html', {'favorit' : favorit})
    else:
        return redirect('/sign-in')


@login_required
def favorit_info_view(request, id):
    if request.method == 'GET':
        favorit = Favorit.objects.get(id=id)
        favorit_image = Favorit.objects.all()
        context = {
            'favorit': favorit,
            'favorit_img': favorit_image,
            'id': id,
        }
        return render(request, 'favorites_info.html', context)

    elif request.method == 'POST':
        favorit = Favorit.objects.get(id=id)
        photo = PhotoModel()
        photo.user = request.user
        photo.save()
        
        favorit.delete()
      
        return redirect('/favorit')


@login_required
def restore(request, id):
    if request.method == 'GET':
        trash_photo = Trash.objects.get(id=id)
        trash_image = Trash.objects.all()
        context = {
            'trash': trash_photo,
            'trash_img': trash_image,
            'id': id,
        }
        return render(request, 'restore.html', context)

    elif request.method == 'POST':
        trash = Trash.objects.get(id=id)
        photo = PhotoModel()
        photo.user = request.user
        photo.img = trash.trash_img
        photo.save()
        
        trash.delete()
      
        return redirect('/trash')



# ???????????????
# def get_photo_info(img_name) :
#         image_path = "media\\" + str(img_name)
#         image = Image.open(image_path) #????????? ?????? ?????? ?????? ?????? ??????
#         info = image._getexif()
#         image.close()

#         taglabel = {}

#         for tag, value in info.items():
#             decoded = TAGS.get(tag, tag)
#             taglabel[decoded] = value

#         print(taglabel['DateTimeOriginal'])  # ?????? ??????
#         print(taglabel['Make'], taglabel['Model'])  # ????????? ??????

#         # ?????? ??????
#         exifGPS = taglabel['GPSInfo']
#         latData = exifGPS[2]  # ??????(latitude)??? ????????????
#         lonData = exifGPS[4]  # ??????(longitude)??? ????????????

#         # ???(Degree), ???(Minute), ???(Second) ??????
#         latDeg = latData[0]
#         latMin = latData[1]
#         latSec = latData[2]

#         lonDeg = lonData[0]
#         lonMin = lonData[1]
#         lonSec = lonData[2]

#         # ???, ???, ?????? ????????????
#         Lat = str(int(latDeg)) + "??" + str(int(latMin)) + "'" + str(latSec) + "\"" + exifGPS[1]
#         Lon = str(int(lonDeg)) + "??" + str(int(lonMin)) + "'" + str(lonSec) + "\"" + exifGPS[3]

#         print(Lat, Lon)

#         # ??? decimal??? ????????????
#         # ?????? ??????
#         Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
#         # ??????, ??????????????? ??????, ????????? ?????? -??? ??????
#         if exifGPS[1] == 'S': Lat = Lat * -1

#         # ?????? ??????
#         Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
#         # ??????, ??????????????? ??????, ????????? ?????? -??? ??????
#         if exifGPS[3] == 'W': Lon = Lon * -1