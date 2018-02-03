from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)
    real_name = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
    addr = models.TextField()
    email = models.EmailField()
    head_url = models.FileField('头像',upload_to='./upload')

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Users)
    content = models.TextField()
    score = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name