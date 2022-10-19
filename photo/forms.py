from django.forms import ModelForm
from django import forms
from .models import PhotoModel

class ImageUpload(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ['imgfile']