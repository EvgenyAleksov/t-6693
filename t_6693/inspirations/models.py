from django.db import models  # type: ignore


class Inspiration(models.Model):
    descr = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']
