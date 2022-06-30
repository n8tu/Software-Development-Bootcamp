from django.shortcuts import render ,HttpResponse
from datetime import datetime

def index(request):
    today = datetime.now()
    context = {
        'Date': today.strftime('%B %d, %Y'),
        'Time': today.strftime('%H:%M %p')
    }
    return render(request,'index.html',context)
