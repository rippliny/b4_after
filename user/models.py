from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    class Meta:
        db_table = "user"

    first_name = models.CharField(max_length=16, null=False)
    last_name = models.CharField(max_length=16, null=False)
    
    def __str__(self):
        return self.username