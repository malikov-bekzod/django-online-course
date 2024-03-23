from django.views import View
from django.shortcuts import render
from blog.models import Blog
from course.models import Category, Course
from teacher.models import Teacher, Speciality


class HomePageView(View):
    def get(self, request):
        categories = Category.objects.all()
        courses = Course.objects.all()
        teachers = Teacher.objects.all()
        blogs = Blog.objects.all()
        context = {
            "categories": categories,
            "courses": courses,
            "teachers": teachers,
            "blogs": blogs,
        }
        return render(request, "home.html", context)
