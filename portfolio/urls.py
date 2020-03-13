from django.urls import path
from . import views
from django.http.request import *

urlpatterns = [
    path('github', views.github(request=HttpRequest()), name="GitHub"),
]