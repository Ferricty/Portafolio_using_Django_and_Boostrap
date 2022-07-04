from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='blog/images')
    date=models.DateField(datetime.date.today)

    class Meta:
        verbose_name="post"
        verbose_name_plural="posts"
