from django.shortcuts import render , redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validation(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect("/") 
        else:
            hash_pass = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
            user = User.objects.create(
                fname = request.POST['fname'],
                lname = request.POST['lname'],
                email = request.POST['email'],
                password = hash_pass
            )
            user.save()
            messages.success(request,"User successfully added!")

            request.session['user_id'] = user.id
            return redirect('/dashboard')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validation(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect("/")
        else:
            userid = User.objects.get(email__iexact=request.POST['email'])
            request.session['user_id'] = userid.id
            return redirect('/dashboard')

    return redirect('/') 

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'your_trips':Trip.objects.filter(joined_the_trip__id = request.session['user_id']).order_by("created_at"),
        'others_trips':Trip.objects.all().exclude(joined_the_trip__id = request.session['user_id']).order_by("created_at"),
    }
    return render(request,'dashboard.html',context)

def logout(request):
    if 'user_id' not in request.session:
        return redirect('/')

    del request.session['user_id']
    return redirect('/')

def new_trip(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request,'new_trip.html',context)

def create_trip(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        errors = Trip.objects.validation(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect(request.META.get('HTTP_REFERER')) 
        else:
            user = User.objects.get(id=request.session['user_id'])
            trip = Trip.objects.create(
                destination = request.POST['destination'],
                start_date = request.POST['start_date'],
                end_date = request.POST['end_date'],
                plan = request.POST['plan'],
                created_by = user
            )
            trip.joined_the_trip.add(user)
            trip.save()
            messages.success(request,"Trip added successfully!")
            return redirect('/dashboard')
    return redirect("/trips/new")

def edit_trip(request,trip_id):
    if 'user_id' not in request.session:
        return redirect('/')
    _trip = Trip.objects.get(id=trip_id)
    if request.session['user_id'] != _trip.created_by.id:
        return redirect('/dashboard')

    context = {
        "trip":_trip,
        'user': User.objects.get(id=request.session['user_id']),
    }

    return render(request,'edit_trip.html',context)

def update_trip(request,trip_id):
    if 'user_id' not in request.session:
        return redirect('/')
        
    trip = Trip.objects.get(id=trip_id)
    if request.session['user_id'] != trip.created_by.id:
        return redirect('/dashboard')

    if request.method == 'POST':
        errors = Trip.objects.validation(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect(request.META.get('HTTP_REFERER')) 
        else:
            trip.destination = request.POST['destination']
            trip.start_date = request.POST['start_date']
            trip.end_date = request.POST['end_date']
            trip.plan = request.POST['plan']
            trip.save()

            messages.success(request,"Trip Updated successfully!")
            return redirect('/dashboard')
    return redirect(f"/trips/update/{trip_id}")

def show_trip(request,trip_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'trip':Trip.objects.get(id=trip_id),
        'user': User.objects.get(id=request.session['user_id']),
    }

    return render(request,'show_trip.html',context)

def join_trip(request,trip_id):
    if 'user_id' not in request.session:
        return redirect('/')

    trip = Trip.objects.get(id=trip_id)
    user = User.objects.get(id=request.session['user_id'])

    user.trips.add(trip)
    user.save()

    return redirect('/dashboard')

def cancel_trip(request,trip_id):
    if 'user_id' not in request.session:
        return redirect('/')

    trip = Trip.objects.get(id=trip_id)
    user = User.objects.get(id=request.session['user_id'])

    user.trips.remove(trip)
    user.save()
    return redirect('/dashboard')

def delete_trip(request,trip_id):
    if 'user_id' not in request.session:
        return redirect('/')

    trip = Trip.objects.get(id=trip_id)
    if trip.created_by.id == request.session['user_id']:
        trip.delete()
    
    return redirect('/dashboard')