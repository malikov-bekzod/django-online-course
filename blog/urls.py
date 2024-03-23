from django.urls import path
from .views import BlogsView,BlogDetailView

urlpatterns = [
    path("", BlogsView.as_view(), name="blogs"),
    path("<int:id>/", BlogDetailView.as_view(), name="blog_detail"),
]
