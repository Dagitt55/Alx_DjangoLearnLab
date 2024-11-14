from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField("year published")

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
    objects = CustomUserManager()
    def __str__(self):
        return self.username

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, date_of_birth=None, profile_photo=None, **extra_fields):
        if not username:
            raise ValueError("The username field must be set")
        user = self.model(username=username, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, date_of_birth=None, profile_photo=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, date_of_birth, profile_photo, **extra_fields)
class Meta:
    permissions = [
        ("can_view", "Can view article"),
        ("can_create", "Can create article"),
        ("can_edit", "Can edit article"),
        ("can_delete", "Can delete article"),
    ]
