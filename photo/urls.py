from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'photo'
urlpatterns = [
    path('upload/', views.fileUpload, name='upload'),
    path('category/', views.category, name='category'),
]
