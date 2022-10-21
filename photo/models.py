from django.db import models
from user.models import UserModel

class Category(models.Model):
    class Meta:
        db_table = "category"
        
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class PhotoModel(models.Model):
    class Meta:
        db_table = "photo"
    
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='photo/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category,default='')


    def __str__(self):
        return self.img.url


class Trash(models.Model):
    class Meta:
        db_table = "trash"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    trash_img = models.ImageField(upload_to='trash/', null=True)


class Favorit(models.Model):
    class Meta:
        db_table = "favorit"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    favorit = models.ImageField(upload_to='favorit/', null=True)
    