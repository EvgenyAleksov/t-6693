from django.db import models  # type: ignore


class Comm(models.Model):

    max_descr = models.TextField(
        blank=True,
        unique=True,
    )

    min_descr_man = models.TextField(
        blank=True,
        unique=True,
    )

    min_descr_wom = models.TextField(
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']
