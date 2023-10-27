from django.shortcuts import render

# Create your views here.
def index(request,path=None):
    return render(request,'menu/index.html',{'menu_name':path})