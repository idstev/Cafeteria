from django.shortcuts import render, get_object_or_404
from .models import Page
# Create your views here.
def pages(request,pageId):
    page=get_object_or_404(Page, id=pageId)
    return render(request, "pages/sample.html", {'page':page})