from django.db import models

class PublishedNewsManager(models.Manager):
    def get_queryset(self):
        from .models import News
        return super().get_queryset().filter(status=News.Status.Published)
