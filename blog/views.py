from django.shortcuts import render
from django.views import View
from .models import Blog, Tag, Comment
from django.db.models import Count

# Create your views here.


class BlogsView(View):
    def get(self, request):
        blogs = Blog.objects.filter(status = "p")
        tags = Tag.objects.all()
        context = {
            "blogs": blogs,
            "tags": tags,
        }
        return render(request, "blog/blogs.html", context)

class BlogDetailView(View):
    def get(self,request,id):
        blog = Blog.objects.get(id=id)
        comments = Comment.objects.filter(blog=blog.id)
        count_comm = Comment.objects.filter(blog=blog.id).count()
        context = {
            "blog": blog,
            "comments": comments,
            "count_comm": count_comm,
        }
        return render(request, "blog/blog_detail.html", context)
