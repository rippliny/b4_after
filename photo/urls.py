from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'photo'
urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('img_info/', views.get_photo_info, name='img_info'),
    # path('category/', views.category, name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
