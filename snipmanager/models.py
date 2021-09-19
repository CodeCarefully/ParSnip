from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django.conf import settings

# https://docs.djangoproject.com/en/3.2/ref/models/fields/


class Snips(TimeStampedModel):
    title = models.CharField(max_length=800)
    data = models.CharField(max_length=10000, null=True)
    encrypted = models.BooleanField(default=False)


    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Snips"
        verbose_name = "Snippet"


