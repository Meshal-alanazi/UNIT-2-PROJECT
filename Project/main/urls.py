from . import views
from django.urls import path 

app_name="main"


urlpatterns = [
    path("contact/",views.contact_view,name="contact_view")
]
