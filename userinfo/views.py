from django.shortcuts import render,redirect
# from .forms import forms
from .forms import RegisterForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login

def register(request):
    
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            
            newUser = User(username=username)
            newUser.set_password(password)
            
            newUser.save()
            
            login(request)
            # return render(request, 'suc.html')
            return redirect("index")
        context={
        "form":form
    }
            
    else:
        form=RegisterForm()
        context={
        "form":form
    }  
    return render(request,"register.html",context)




def login(request):
    return render(request,"login.html")
def logout(request):
    return render(request,"logout.html")

 




