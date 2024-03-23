from django.shortcuts import render
from django.views import View
from .models import Course,Category
# Create your views here.

class CourseListView(View):
    def get(self,request):
        courses = Course.objects.all()
        categories = Course.objects.all()
        context = {
            "courses":courses,
            "categories":categories
        }
        return render(request, "course/course.html",context)
