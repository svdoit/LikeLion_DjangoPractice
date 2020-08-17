from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

# Create your views here.
def mainView(request):
    return render(request, 'main.html')

def blogPostlistView(request):
    blogs = Blog.objects.all()
    return render(request, 'blogPostlist.html', {'blogs':blogs})

def blogDetailView(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogDetail.html', {'blog_detail':blog_detail})

def blogNewView(request):
    return render(request, 'blogNew.html')

def blogCreateView(request):
    blogs = Blog()
    blogs.title = request.POST.get('title')
    blogs.body = requset.POST.get('body')
    blogs.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))