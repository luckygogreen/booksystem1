from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def houseindex(request):
    return HttpResponse('This house index page')