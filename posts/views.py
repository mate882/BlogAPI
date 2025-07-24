from django.shortcuts import render, redirect, get_object_or_404
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

        Post.objects.create(title=title, content=content, image=image, author=request.user)
        return redirect('posts:home')
    return render(request, 'main/create.html')


def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.image = request.FILES.get('image', post.image) 
        post.save()
        return redirect('posts:home')
    return render(request, 'main/update.html', {'post': post})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user.is_authenticated:
        if request.user in post.likes.all():
            post.likes.remove(request.user)  
        else:
            post.likes.add(request.user)     
    
    elif not request.user.is_authenticated:
        return redirect('users:login')

    return redirect('posts:home')


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:home')
    return render(request, 'main/delete.html', {'post': post})