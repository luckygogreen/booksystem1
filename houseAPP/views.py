from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
# Create your views here.
def house(request):
    return render(request,'house/house.html')