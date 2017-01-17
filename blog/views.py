from django.shortcuts import render
from django.template import RequestContext
# Create your views here.
from .models import Post

def  ListView(request):
    queryset=Post.objects.all().order_by("-date")[:25]
    return render(request,'blog/blog.html', {'queryset':queryset})