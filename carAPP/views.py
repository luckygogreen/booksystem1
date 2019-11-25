from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
def car(request):
    # return render(request,reverse('carpage'))
    return render(request,'car/car.html')