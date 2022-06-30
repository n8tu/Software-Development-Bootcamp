from django.http import HttpResponse
from django.shortcuts import render , redirect 
import random
from datetime import datetime

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []

    return render(request,'index.html')

def process(request):
    chance = 100
    location = request.GET['location']

    if request.GET['location'] == 'quest':
        generateGold = random.randint(0,50)
        chance = 50
    else:
        generateGold = random.randint(10,20)

    if(random.randint(1,100) <= chance):
        return redirect(f'/increase?gold={generateGold}&location={location}')
    else:
        return redirect(f'/decrease?gold={generateGold}&location={location}')
    
        


def increase(request):
    gold = int(request.GET['gold'])
    location = request.GET['location']

    request.session['gold'] += gold
    request.session['activities'].append(
        f"You entered a {location} and earned {gold} gold. ({datetime.now().strftime('%B %d, %Y %H:%M %p')})"
        )
    request.session.save()
    return redirect('/')

def decrease(request):
    gold = int(request.GET['gold'])
    location = request.GET['location']

    request.session['gold'] -= gold
    request.session['activities'].append(
        f"You failed a {location} and lost {gold} gold. Ouch. ({datetime.now().strftime('%B %d, %Y %H:%M %p')})"
        )
    request.session.save()
    return redirect('/')


def destroy(request):
    try:
        del request.session['gold']
        del request.session['activities']
        return redirect('/')
    except:
        return HttpResponse("No sessions found")