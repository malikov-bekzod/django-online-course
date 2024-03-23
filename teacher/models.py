from django.db import models


# Create your models here.
class Speciality(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="teachers/")
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    telegram_link = models.URLField(max_length=250, null=True, blank=True)
    instagram_link = models.URLField(max_length=250, null=True, blank=True)
    linkedin_link = models.URLField(max_length=250, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
