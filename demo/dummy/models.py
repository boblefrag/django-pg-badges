from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Sketch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    hit_views = models.PositiveIntegerField()
