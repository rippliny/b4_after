from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    first_name = models.CharFiled(null=False)
    last_name = models.CharFiled(null=False)