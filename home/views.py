from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from products.models import Post
from .forms import ContactUsForm


def home(req):
    return render(req,'home/index.html')


def about(req):
    return render(req,"home/about.html")

def faq(req):
    return render(req,"home/faq.html")


def contact(req):
    if req.method == 'GET':
        return render(req,"home/contact.html")
    
    elif req.method == 'POST':
        form = ContactUsForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(req.path_info)

# Create your views here.
