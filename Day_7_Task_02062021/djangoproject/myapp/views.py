from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse('<h1>Welcome to Home Page</h1>')

def aboutpageview(request):
    return HttpResponse('Welcome to About Us Page')

def contactpageview(request):
    return HttpResponse('Welcome to Contact Us Page')
