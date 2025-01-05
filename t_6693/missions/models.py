from django.db import models  # type: ignore


class Mission(models.Model):

    descr = models.TextField(
        max_length=10000,
        blank=True,
    )

    def __str__(self):
        return self.id
