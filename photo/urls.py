from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [
    path('upload/', views.fileUpload, name='upload'),
    # path('photo/', views.upload_image),
    path('category/', views.main_cateory),
]