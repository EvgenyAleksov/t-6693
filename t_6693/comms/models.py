from django.db import models  # type: ignore


class Comm(models.Model):

    descr = models.TextField(
        blank=True,
    )

    descr_man = models.TextField(
        blank=True,
    )

    descr_wom = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']
