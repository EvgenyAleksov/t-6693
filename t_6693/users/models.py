from django.contrib.auth.models import AbstractUser  # type: ignore

# from django.db import models # type: ignore


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username