from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func(request):
    peoples = [
        {"name":"Abhijeet", "age": 16},
        {"name":"Raghav Singhal","age":22},
        {"name":"Rohit Sharma","age":17}
    ]
    print(peoples[2])
    return render(request,"index.html",context={'page':'Home',"peopless":peoples})

def func1(request):
    print("")
    context = {'page':'contact'}
    return render(request,"contact.html",context)

def func2(request):
    print("")
    context = {'page':'about'}
    return render(request,"about.html",context)