from django.shortcuts import render
from . models import Post, User

def feed(request):
    posts = Post.objects.all()
    users = User.objects.all()
    context = {
        'posts': posts,
        'users': users
    }
    return render(request, 'home\\feed.html', context)

def network(request):
    return render(request, 'home\\network.html') 

def jobs(request):
    return render(request, 'home\\jobs.html')

def message(request):
    return render(request, 'home\\message.html')

def notification(request):
    return render(request, 'home\\notification.html')

def home(request):
    return render(request, 'home\\home.html')