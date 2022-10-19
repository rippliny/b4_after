from django.shortcuts import render, redirect
from .models import PhotoModel
from .forms import ImageUpload


def fileUpload(request):
    if request.method == 'POST':
        photo = PhotoModel()
        user = request.user

        photo.user = user
        photo.imgfile = request.FILES["imgfile"]
        photo.save()

        return redirect('/upload')
    else:
        imageupload = ImageUpload
        context = {
            'imageupload': imageupload,
        }
        return render(request, 'upload.html', context)