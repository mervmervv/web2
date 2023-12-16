from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
   return render(request,'pages/index.html') 

def about(request):
   return render(request,'pages/about.html') 

def galeri(request):
   return render(request,'pages/galeri.html') 

def call(request):
   return render(request,'pages/call.html') 

def duyuru(request):
   return render(request,'pages/duyuru.html') 

def iletisim(request):
   return render(request,'pages/iletisim.html') 

def project(request):
   return render(request,'pages/project.html') 

def login(request):
   return render(request,'pages/login.html') 

def signin(request):
   return render(request,'pages/signin.html') 

def curlingtr(request):
   return render(request,'pages/curlingtr.html') 

def sportstr(request):
   return render(request,'pages/sportstr.html') 
    
def duyuru1(request):
   return render(request,'pages/duyuru1.html') 
