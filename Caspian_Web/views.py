from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("home")


def about_us(request):
    return HttpResponse('Hello world!!')
