from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [
    path('upload/', views.fileUpload, name='upload'),
    path('category/', views.category, name='category'),

]