from django.shortcuts import render

def index(request):
    return render(request, "login\index.html")

def signup(request):
    return render(request, "login\signup.html")