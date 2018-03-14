
# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm



def listen(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/listen.html', {'posts': posts})


def listru(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/listru.html', {'posts': posts})
