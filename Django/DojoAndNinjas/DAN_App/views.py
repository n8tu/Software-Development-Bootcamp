from django.shortcuts import render, redirect
from .models import *

def index(request):
    dojos = Dojo.objects.all()
    context = {
        "dojos":dojos,
    }
    return render(request,'index.html',context)

def create(request):
    if request.method == 'POST':
        if(request.POST['form'] == 'add_Dojo'):
            newDojo = Dojo.objects.create(
                name = request.POST['dojo_name'],
                ciry = request.POST['dojo_city'],
                state = request.POST['dojo_state']
            )
            newDojo.save()
        elif(request.POST['form'] == 'add_Ninja'):
            dojo = Dojo.objects.get(id=int(request.POST['dojo_id']))
            newNinja = Ninja.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                dojo_id = dojo,
            )
            newNinja.save()
        else:
            pass
    
    return redirect('/')
