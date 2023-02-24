from django.db import models


class CeleryDebugObject(models.Model):
    data: models.CharField = models.CharField(
        max_length=50,
    )
