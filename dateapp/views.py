from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request,'home.html')

def YesView(request):
    return render(request,'yes.html')