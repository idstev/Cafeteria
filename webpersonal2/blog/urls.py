from django.urls import path
from . import views
urlpatterns = [

    path("", views.blog, name="blog"),
    path("category/<int:categoryId>/", views.category, name="category"),
]
