from django.db import models


# Create your models here.

class MovieInfo(models.Model):
    no = models.CharField(max_length=20, verbose_name="编号")
    url = models.CharField(max_length=30, verbose_name="地址")
    title = models.CharField(max_length=20, verbose_name="标题")
    desc = models.CharField(max_length=20, verbose_name="导演")
    grade = models.CharField(max_length=5, verbose_name="评分")
