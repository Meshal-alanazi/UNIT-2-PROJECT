from django.shortcuts import render,redirect


from django.http import HttpRequest,HttpResponse
from .models import Contact

# Create your views here.

def contact_view(request:HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Received data - Name: {name}, Email: {email}, Message: {message}")

        if email:  
            contact = Contact(
                name=name,
                email=email,
                message=message
            )
            contact.save()
        else:
            print("Email is missing!") 
        return redirect('main:contact_view')
    return render(request, "main/contact.html")
