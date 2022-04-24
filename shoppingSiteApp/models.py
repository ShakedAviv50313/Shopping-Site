from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=30)
    tags = TaggableManager()
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=30)
    time_added = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(
        upload_to='static/images', default='satic/image/no_pic.png')

    def __str__(self):
        return self.name
