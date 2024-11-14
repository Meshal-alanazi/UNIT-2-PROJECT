from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Project
from main.models import Contact



# Create your views here.
def dashboard_view(request:HttpRequest):
 if request.method == "POST":
   
   new_project=Project(title=request.POST["title"],about=request.POST["about"],image=request.FILES["image"] if "image" in request.FILES else None,category=request.POST["category"])

   new_project.save()
   return redirect('about:project_view')
 return render(request,"main/dashboard.html")
   


def project_update(request:HttpRequest,proj_id:int):

     proj= Project.objects.get(pk=proj_id)
     if request.method == "POST":
         proj.title = request.POST["title"]
         proj.about = request.POST["about"]
        
       
         if "image" in request.FILES: proj.image = request.FILES["image"]
         proj.save()
       

         return redirect("dashboard:dashboard_view", proj_id=proj.id)
     
     return render(request, "main/project_update.html", {"proj" : proj})