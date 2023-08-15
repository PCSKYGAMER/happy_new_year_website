from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'index.html')

def ticket(request):
    return render(request,'ticket.html')