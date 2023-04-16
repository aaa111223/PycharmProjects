from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    re = 'aaa'
    print('body ')
    return HttpResponse('This is test page!')


def blog_articles(request, num):
    num = 1
    return HttpResponse('hello')


def comments(request):
    return HttpResponse('OK')
