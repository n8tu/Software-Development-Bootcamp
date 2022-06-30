from django.http import JsonResponse
from django.shortcuts import redirect, render, HttpResponse

def redirectMethod(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}" )

def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    return redirect('/blogs')

def json(request):
    return JsonResponse({
        'titel':'My First Blog',
        'content': "Sint excepteur voluptate cupidatat duis ea. Irure veniam consectetur sit est dolore ipsum aute commodo eiusmod deserunt deserunt qui exercitation. Cillum tempor minim ullamco aute elit nisi ad labore culpa anim veniam consequat. Nisi deserunt duis ut ipsum non sunt ad id exercitation ipsum commodo Lorem. Ut commodo reprehenderit enim est. Irure Lorem nostrud consequat sit. Do est amet eiusmod duis id do consequat do laborum aliquip reprehenderit."
    })

