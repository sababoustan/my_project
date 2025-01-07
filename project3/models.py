from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    counted_views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title


# Create your models here.
