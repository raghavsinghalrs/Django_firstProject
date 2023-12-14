from django.shortcuts import render

# Create your views here.

def reciepes(request):
    return render(request,"recipes.html")