from django.contrib.auth.models import AbstractUser  # type: ignore


class User(AbstractUser):
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
