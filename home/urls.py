from django.urls import path
from . import views

urlpatterns = [
    path("feed", views.feed, name="feed"),
    path("network", views.network, name="network"),
    path("notification", views.notification, name="notification"),
    path("jobs", views.jobs, name="jobs"),
    path("home", views.home, name="home"),
    path("message", views.message, name="message"),
]
