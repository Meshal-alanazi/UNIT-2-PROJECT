from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home_view(reuqest:HttpRequest):

    return render(reuqest,"main/index.html")


def portfolio_view(request:HttpRequest):
    return render (request,"main/portfolio.html")


def story_view(request:HttpRequest):
    return render(request,"main/story.html")






def project_view(request:HttpRequest):

    return render(request,"main/project.html")