from django.db import models  # type: ignore


class Mission(models.Model):

    descr = models.TextField(
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']
