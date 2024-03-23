from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 250,null=True)
    course_count = models.PositiveIntegerField(default = 1)
    image = models.ImageField(upload_to="course/category_pictures/")
    created_date = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    student_count = models.PositiveIntegerField(default=1)
    duration = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to="course/course_pictures/")
    created_date = models.DateTimeField(auto_now_add=True)



