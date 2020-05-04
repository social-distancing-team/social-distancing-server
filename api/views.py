from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
    user = User(username='mark')
    user.save()
    all_Users = User.collection.fetch()
    for u in all_Users:
        print("{}:{}".format(u.id, u.username))
    return HttpResponse("<h1>Home</h1>")
