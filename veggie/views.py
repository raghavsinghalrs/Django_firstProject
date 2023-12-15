from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        reciepe_images = request.FILES.get('reciepe_images')
        reciepe_name = data.get('reciepe_name')
        reciepe_desc = data.get('reciepe_desc')
        print("name :",reciepe_name) 
        print("description :",reciepe_desc)
        print(reciepe_images)

        reciepe.objects.create(
            reciepe_name=reciepe_name,
            reciepe_desc=reciepe_desc,
            reciepe_images=reciepe_images,
        )
        return redirect("/receipes/")
    
    query = reciepe.objects.all()
    if request.GET.get('search'):
        query = query.filter(reciepe_name__icontains = request.GET.get('search'))
    context = {'receipes': query}
    return render(request,"recipes.html",context)

def delete_receipe(request,id):
    query = reciepe.objects.get(id=id)
    query.delete()
    return redirect("/receipes/")


def update_receipe(request,id):
    query = reciepe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        reciepe_images = request.FILES.get('reciepe_images')
        reciepe_name = data.get('reciepe_name')
        reciepe_desc = data.get('reciepe_desc')
        query.reciepe_name = reciepe_name
        query.reciepe_desc=reciepe_desc
        if reciepe_images:
            query.reciepe_images=reciepe_images
        query.save()
        return redirect("/receipes/")
        
    context = {'receipes':query}
    return render(request,"update_reciepes.html",context)
