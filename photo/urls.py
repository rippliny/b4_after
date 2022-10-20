from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'photo'
urlpatterns = [
    path('upload/', views.fileUpload, name='upload'),
    path('img_info/<int:id>/', views.img_info, name='img_info'),
    path('img_info/<int:id>/delete', views.img_info, name='delete'),
    path('photo/favorit/<int:id>/', views.favorites, name='favorites'),
    path('trash/', views.trash, name='trash'),

    # path('category/', views.category, name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
