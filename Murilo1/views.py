from django.shortcuts import render 

# Create your views here.
def index(request):#defino função 
    return render(request, 'index.html')#retorno a importação render