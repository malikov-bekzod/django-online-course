from django.shortcuts import render
from django.views import View
from .models import Teacher
# Create your views here.
class TeacherView(View):
    def get(self,request):
        teachers = Teacher.objects.all()
        context = {
            "teachers":teachers
        }
        return render(request, "teacher/teachers.html", context)