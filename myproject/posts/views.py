from django.shortcuts import render, redirect
from .models import Post

def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'feed.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        Post.objects.create(
            user=request.user,
            content=request.POST['content']
        )
        return redirect('feed')