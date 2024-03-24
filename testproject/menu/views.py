from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def demo(request):
    return render(request, 'demo.html')
