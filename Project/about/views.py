from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from dashboard.models import Project

# Create your views here.

def home_view(reuqest:HttpRequest):

    return render(reuqest,"main/index.html")


def portfolio_view(request: HttpRequest):
    proj = Project.objects.all()
    return render(request, "main/portfolio.html", {"proj": proj})

    


def story_view(request:HttpRequest):
    return render(request,"main/story.html")




def post_detail(request:HttpRequest, proj_id:int):

    proj= Project.objects.get(pk=proj_id)
    similarProject = Project.objects.filter(category=proj.category)[0:3]
    response = render(request, 'main/detail.html', context={"proj":proj, " similarProject":  similarProject})

    return response


def game_view(reuqest:HttpRequest):

    return render(reuqest,"main/games.html")
