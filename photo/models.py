from django.db import models
from user.models import UserModel


class PhotoModel(models.Model):
    class Meta:
        db_table = "photo"
        
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    imgfile = models.ImageField(upload_to='photo/', null=True, blank=True)

class CategoryModel(models.Model):
    class Meta:
        db_table = 'category'

    image = models.ForeignKey(PhotoModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=24, null=True)

