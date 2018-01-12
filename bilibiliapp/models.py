from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=1000, blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(Tags, blank=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('blog:details', kwargs={'pk': self.pk})


class BilibiliApp(models.Model):

    pic_id = models.IntegerField()
    img_url = models.CharField(max_length=1000)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)


