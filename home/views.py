from django.shortcuts import render

def home(req):
    return render(req,'home/index.html')

# Create your views here.
