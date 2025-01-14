from django.db import models  # type: ignore


class Comp_Comm(models.Model):
    name = models.CharField(
        max_length=2,
        unique=True,
        blank=False,
    )

    descr_1 = models.TextField(
        blank=True,
    )

    descr_2 = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.id
    
    class Meta:
        ordering = ['name']

