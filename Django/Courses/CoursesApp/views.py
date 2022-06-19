from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    _courses = Course.objects.all()
    context = {
        'courses':_courses
    }
    return render(request,'index.html',context)

def create_course(request):
    if request.method == 'POST':
        errors = Course.objects.validate(request.POST)
        description_errors = Description.objects.validate(request.POST)
        errors.update(description_errors) # add description_error key , value to the first dict

        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
        else:
            _description = Description.objects.create(
                description = request.POST['description'],
            )
            _course = Course.objects.create(
                course_name = request.POST['course_name'],
                course_description = _description,
            )   
            _course.save()
            _description.save()
            messages.success(request,"Added successfully")
            
    return redirect('/')

def destroy_course(request,_id):
    course = Course.objects.get(id=_id)
    course.delete()
    return redirect("/")
            
