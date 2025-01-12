from django.contrib.auth.models import AbstractUser  # type: ignore


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['id']

