from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE, related_name='Профиль')
    phone = models.IntegerField(unique=True)
    image_profile = models.ImageField(
        verbose_name='Фотография', upload_to='profile/')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
