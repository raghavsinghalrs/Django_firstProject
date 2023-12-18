from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        reciepe_images = request.FILES.get('reciepe_images')
        reciepe_name = data.get('reciepe_name')
        reciepe_addby = request.user.username
        reciepe_desc = data.get('reciepe_desc')
        print("name :",reciepe_name) 
        print("description :",reciepe_desc)
        print(reciepe_images)

        reciepe.objects.create(
            reciepe_name=reciepe_name,
            reciepe_desc=reciepe_desc,
            reciepe_addby=reciepe_addby,
            reciepe_images=reciepe_images,
        )
        return redirect("/receipes/")
    
    query = reciepe.objects.all()
    placeholder = ""
    if request.GET.get('search'):
        placeholder = request.GET.get('search')
        print(placeholder)
        query = query.filter(reciepe_name__icontains = request.GET.get('search'))
    context = {'receipes': query,'placeholder':placeholder}
    return render(request,"recipes.html",context)

@login_required(login_url="/login/")
def delete_receipe(request,id):
    query = reciepe.objects.get(id=id)
    query.delete()
    return redirect("/receipes/")

@login_required(login_url="/login/")
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

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,"Invalid username")
            return redirect('/login/')
        user = authenticate(username = username, password=password)

        if user is None:
            messages.info(request, 'Invalid Password')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/receipes/')
    return render(request,"login.html")

@login_required(login_url="/login/")
def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register/')
        if username is not None:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
            )
            user.set_password(password)
            user.save()
            messages.info(request, "You are successfully registered")
            return redirect("/login/")
        else:
            # Handle the case where username is not provided
            return render(request, "register.html", {"error_message": "Username is required."})

    return render(request, "register.html")
