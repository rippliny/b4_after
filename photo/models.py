from django.db import models
from user.models import UserModel

class PhotoModel(models.Model):
    class Meta:
        db_table = "photo"
    
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='photo/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorites = models.ManyToManyField(UserModel, related_name='favorites' ,blank=True)
    trash = models.ManyToManyField(UserModel, related_name='trash' ,blank=True)
    category = models.CharField(max_length=16, null=True, default='')

    def __str__(self):
        return 'id : {}'.format(self.id)