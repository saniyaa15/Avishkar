from django.shortcuts import render,redirect
from .form import *
from .models import *

# Create your views here.
def index(req):
    return render(req,'index.html')

def contactus(req):
    if req.method=="POST":
       obj=ContactUsForm(req.POST)
       obj.save() 
       return redirect('home:contactus')
    else :
        obj=ContactUsForm()
        return render(req,'contactus.html',{'form':obj})

def aboutus(req):
    return render(req,'aboutus.html')

def products(req):
    return render(req,'products.html')

def addproduct(req):
    if req.method=="POST":
        obj=AddProductForm()
        obj.save()
        return redirect('home:addproduct')
    else :
        obj=AddProductForm()
        return render(req,'addproduct.html',{'form':obj})
