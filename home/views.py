from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Post, User
from .forms import PostForm

def feed(request):
    if request.POST:
        print(request.user)
        # user = User.objects.get(username=request.user.username)
        user = User.objects.get(id=2) 
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Post(photo=request.FILES['photo'], description=request.POST['description'], user=user)
            print(instance)
            instance.save()


    posts = Post.objects.all().order_by('-post_date')
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
    posts = Post.objects.all().order_by('-post_date')
    users = User.objects.all()

    context = {
        'users': users,
        'posts': posts
    }
    return render(request, 'home\\home.html', context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def like(request):
    if request.method == 'POST' and is_ajax(request): 
        # 2 -> request.user.id
        user = User.objects.get(id=2)
        flag = None
        post_id = int(request.POST.get('post_id'))
        post_obj = get_object_or_404(Post, id=post_id)

        if post_obj.like.filter(id=2).exists():
            # post_obj.like.remove(request.user)
            post_obj.like.remove(user)
            post_obj.save()
            flag = False
        else:
            # post_obj.like.add(request.user)     
            post_obj.like.add(user)
            post_obj.save()
            flag = True
        return JsonResponse({'flag': flag})
    
    return HttpResponse("Error access denied")