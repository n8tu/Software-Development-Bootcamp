from django.shortcuts import render, redirect
from .models import *

def index(request):
    return redirect('/shows')

def shows(request):
    all_shows = Show.objects.all()
    context = {
        'shows':all_shows,
    }
    return render(request,'all_shows.html',context)

def show_new(request):
    return render(request,'create_show.html')

def create_show(request):
    if request.method == 'POST':
        show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description']
        )
        show.save()
        return redirect(f'/shows/{show.id}')

    return redirect('/')

def show(request,_id):
    _show = Show.objects.get(id=_id)
    context = {
        'show':_show,
    }
    return render(request,'show.html',context)


def show_edit(request,_id):
    show = Show.objects.get(id=_id)
    context = {
        'show':show,
    }
    return render(request,'edit_show.html',context)

def show_update(request,_id):
    if request.method == 'POST':
        show = Show.objects.get(id=_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.description = request.POST['description']
        show.release_date = request.POST['release_date']
        show.save()
    
    return redirect(f'/shows/{_id}')

def show_destory(request,_id):
    show = Show.objects.get(id=_id)
    show.delete()

    return redirect('/shows')





