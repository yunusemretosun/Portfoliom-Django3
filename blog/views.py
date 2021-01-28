from django.shortcuts import render,get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all().order_by("-date")[:]
    return render(request,'blog/all_blog.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_object = get_object_or_404(Blog , pk=blog_id) #gelen blog_id ile databasetekini karsilastiriyor.
    return render(request,'blog/detail.html',{'blog':blog_object})#ve objeyi cagrilan yere gonderiyor.