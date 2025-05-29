from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'main/home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        Post.objects.create(title=title, content=content, image=image)
        return redirect('posts:home')
    return render(request, 'main/create.html')