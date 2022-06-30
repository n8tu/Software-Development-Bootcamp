from django.http import JsonResponse
from django.shortcuts import render , HttpResponse

def index(request):
    return render(request,'index.html')

def create(request):
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    gender = request.POST['gender']
    skills = request.POST.getlist('skills[]')
    context = {
        'name':name,
        'location':location,
        'language':language,
        'comment':comment,
        'gender':gender,
        'skills':skills,
    }
    
    return render(request,'show.html',context)
