from django.http import HttpResponse
from django.shortcuts import redirect, render
import random

def index(request):
    if not "my_number" in request.session:
        request.session['my_number'] = random.randint(0,100)
    return render(request,'index.html')

def guess(request):
    if request.POST['guess']:
        inputGuess = int(request.POST['guess'])

        if(request.session['my_number'] == inputGuess):
            request.session['alert'] = "success"
            request.session['message'] = f"{request.session['my_number']} was the number!"

        elif(request.session['my_number'] < inputGuess):
            request.session['alert'] = "danger"
            request.session['message'] = f"Too High!"


        else:
            request.session['alert'] = "danger"
            request.session['message'] = "Too Low!"
    
    return redirect('/')

def destroy(request):
    try:
        del request.session['alert']
        del request.session['message']
        del request.session['my_number']
        return redirect('/')
    except:
        return HttpResponse("No sessions found!")
