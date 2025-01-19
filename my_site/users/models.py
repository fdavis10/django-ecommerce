from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    image = models.ImageField(upload_to="users_avatars_default", blank=True, null=True)

    class Meta:
        db_table = 'user'
    
    def __str__(self):
        return self.username 