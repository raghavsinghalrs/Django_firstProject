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
    return render(request,"index.html",context={"peopless":peoples})

def func1(request):
    print("")
    return render(request,"contact.html")

def func2(request):
    print("")
    return render(request,"about.html")