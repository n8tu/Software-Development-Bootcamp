from django.shortcuts import render , redirect
from .models import Users

def index(request):
    users = Users.objects.all()
    context = {
        "Users":users,
    }
    return render (request,"index.html",context)

def create(request):
    newUser = Users.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        age = request.POST['age'],
    )
    newUser.save()
    return redirect("/")
