from . import views
from django.urls import path


app_name="about"

urlpatterns = [
    path("",views.home_view,name="home_view"),
    path("portfolio/",views.portfolio_view,name="portfolio_view"),
    path("story/",views.story_view,name="story_view"),
    path("detail/<proj_id>/",views.post_detail,name="post_detail"),
   
]