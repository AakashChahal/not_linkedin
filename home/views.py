from django.shortcuts import render

def feed(request):
    return render(request, 'home\\feed.html')

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