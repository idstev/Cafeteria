from django.urls import path
from . import views
urlpatterns = [
    path("<int:pageId>/", views.pages, name="pages"),
]
