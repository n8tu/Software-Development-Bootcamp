from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    return redirect('/shows')


def shows(request):
    all_shows = Show.objects.all()
    context = {
        'shows': all_shows,
    }
    return render(request, 'all_shows.html', context)


def show_new(request):
    return render(request, 'create_show.html')


def create_show(request):
    if request.method == 'POST':

        errors = Show.objects.show_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            show = Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release_date'],
                description=request.POST['description']
            )
            show.save()
            messages.success(request, "Show successfully Added!")
            return redirect(f'/shows/{show.id}')

    return redirect('/shows/new')


def show(request, _id):
    _show = Show.objects.get(id=_id)
    context = {
        'show': _show,
    }
    return render(request, 'show.html', context)


def show_edit(request, _id):
    show = Show.objects.get(id=_id)
    context = {
        'show': show,
    }
    return render(request, 'edit_show.html', context)


def show_update(request, _id):
    if request.method == 'POST':
        errors = Show.objects.show_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            show = Show.objects.get(id=_id)
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.description = request.POST['description']
            show.release_date = request.POST['release_date']
            show.save()
            return redirect(f'/shows/{_id}')

    return redirect(f'/shows/{_id}/edit')


def show_destory(request, _id):
    show = Show.objects.get(id=_id)
    show.delete()

    return redirect('/shows')


def create_show_ajax(request):
    if request.method == 'POST':

        errors = Show.objects.show_validator(request.POST)

        if len(errors) > 0:
            data = {
                'message':errors,
                'alert':"danger"
            }
        else:
            show = Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release_date'],
                description=request.POST['description']
            )
            show.save()
            data = {
                'message':{"success":"Show successfully Added!"},
                'alert':"success"
            }

        return JsonResponse(data)

def update_show_ajax(request,_id):
    if request.method == 'POST':
        errors = Show.objects.show_validator(request.POST)
        if len(errors) > 0:
            data = {
                'message':errors,
                'alert':"danger"
            }
        else:
            show = Show.objects.get(id=_id)
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.description = request.POST['description']
            show.release_date = request.POST['release_date']
            show.save()
            data = {
                'message':{"success":"Show successfully Added!"},
                'alert':"success"
            }
        return JsonResponse(data)

