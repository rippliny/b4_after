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
