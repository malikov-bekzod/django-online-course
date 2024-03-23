from django.db import models
from teacher.models import Teacher
from django.contrib.auth.models import User


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 60)
    def __str__(self):
        return self.name

class BlogStatus(models.TextChoices):
    publish = ("p", "Publish",)
    draft = ("d", "Draft",)

class Blog(models.Model):
    title = models.CharField(max_length = 250)
    text = models.TextField()
    image = models.ImageField(upload_to="blog/blog-pictures/")
    status = models.CharField(max_length = 5, choices = BlogStatus, default = BlogStatus.publish)
    author = models.ForeignKey(Teacher,on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class BlogTag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text[:10]
