from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, phone_number, password):
        user = self.model(
            username=username,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, phone_number, password):
        user = self.create_user(username, phone_number, password)
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_superuser
