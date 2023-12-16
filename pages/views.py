from django.shortcuts import render
from .models import project_page


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
 




def project_pages(request, project_url):
   
   ProjectPage = project_page.objects.all()

   context = {
     'project_page_content': ProjectPage
   }

   return render(request,'pages/project_page.html', context) 

    


def duyuru1(request):
   return render(request,'pages/duyuru1.html') 
