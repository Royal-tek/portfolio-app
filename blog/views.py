from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
    blog = Blog.objects.all()
    return render(request, 'blog/home.html', {'blog': blog})

def detail(request, blog_id):
    '''
    or instead of using the objects.get you can use 
    blogdetails = get_objects_or_404(Blog, pk= blog_id)
    '''
    blogdetail = Blog.objects.get(pk = blog_id)
    return render(request, 'blog/detail.html', {'blog':blogdetail})