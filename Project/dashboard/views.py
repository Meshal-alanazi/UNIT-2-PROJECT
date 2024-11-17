from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Project
from main.models import Contact
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden



# Create your views here.
def dashboard_view(request: HttpRequest):
    proj = Project.objects.all()
    return render(request, "main/dashboard.html", {"proj": proj})


   
def new_project(request:HttpRequest):
 if request.method == "POST":
   
   new_project=Project(title=request.POST["title"],about=request.POST["about"],image=request.FILES["image"] if "image" in request.FILES else None,category=request.POST["category"])

   new_project.save()
   return redirect('about:portfolio_view')
 return render(request,"main/add.html")

def project_update(request:HttpRequest,proj_id:int):

     proj= Project.objects.get(pk=proj_id)
     if request.method == "POST":
         proj.title = request.POST["title"]
         proj.about = request.POST["about"]
         proj.category = request.POST["category"]
         
        
       
         if "image" in request.FILES: proj.image = request.FILES["image"]
         proj.save()
       

         return redirect("dashboard:dashboard_view")
     
     return render(request, "main/project_ubdate.html", {"proj" : proj})




def project_delete(request: HttpRequest, proj_id: int):
    if request.method == "POST":
        proj = get_object_or_404(Project, pk=proj_id)
        proj.delete()
        return redirect('dashboard:prject_view')
    return HttpResponseForbidden("Invalid request method.")


def Messages_view(request: HttpRequest):

    contact = Contact.objects.all()
 
    return render(request, 'main/message.html', context={'contact': contact})
    


      

  

   


def prject_view(request:HttpRequest):
     proj = Project.objects.all()
     return render(request, "main/project_view.html", {"proj": proj})

def message_delete(request:HttpRequest,contact_id):
    if request.method == "POST":
        contact= get_object_or_404(Contact, pk=contact_id)
        contact.delete()
        return redirect('dashboard:Messages_view')
    return HttpResponseForbidden("Invalid request method.")