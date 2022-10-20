from django.contrib import admin
from .models import PhotoModel, Category


admin.site.register(PhotoModel)
admin.site.register(Category)