from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password
from notes_keeper import settings
from .manager import *




class CustomUser(AbstractBaseUser, PermissionsMixin):
    # username=None
    # first_name=None
    # last_name=None
    email = models.CharField(max_length=256, unique=True, null=False)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)




class Note(models.Model):
    foreign_key = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length= 256)
    description = models.TextField(null=True, blank= True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


