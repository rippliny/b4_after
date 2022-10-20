from django.db import models
from user.models import UserModel

class PhotoModel(models.Model):
    class Meta:
        db_table = "photo"
    
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='photo/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=16, null=True, default='')
    favorites = models.ManyToManyField(UserModel, related_name='favorites' ,blank=True)


    def __str__(self):
        return 'id : {}'.format(self.id)


class Trash(models.Model):
    class Meta:
        db_table = "trash"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    trash = models.ImageField(upload_to='trash/', null=True)