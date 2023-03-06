from django.http import HttpResponse

from django.shortcuts import render


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'ronoob.html', context)

def hello(request):
    return HttpResponse("Hello world ! ")

def mainpage(request):
    return render(request,'mainpage.html')