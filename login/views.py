from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from home.views import feed
User = get_user_model()

def index(request):
    if request.method == "POST":
        # messages.error(request, "Test Error")
        email = request.POST['email']
        # print(email)
        password = request.POST['password']
        # print(password)

        user = auth.authenticate(email=email, password=password)
        print("user: ", user)
        if user is not None and not user.is_staff:
            auth.login(request, user)
            messages.success(request, "You are logged in")
            return redirect('feed')

        else:
            messages.error(request, "Invalid credentials")
            return redirect('index')

    return render(request, "login\index.html")

def signup(request):
    if request.method == "POST":
        # print("registered")
        name = request.POST['name']
        photo = request.POST['photo']
        email = request.POST['email']
        bio = request.POST['bio']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not password == password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "User already exists")
            return redirect('signup')

        user = User.objects.create_user(name=name, email=email, bio=bio, photo=photo, password=password)
        user.save()
        auth.login(request, user)
        messages.success(request, 'You are registered! You can log in now!')
        return redirect('index')
        
    return render(request, "login\signup.html")