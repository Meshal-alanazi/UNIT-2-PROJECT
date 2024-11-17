from . import views
from django.urls import path


app_name="dashboard"

urlpatterns=[

    path("dashboard/",views.dashboard_view,name="dashboard_view"),
    path("update/<proj_id>/",views.project_update,name="project_update"),
    path("add/",views.new_project,name="new_project"),
    path("delete/<int:proj_id>/", views.project_delete, name="project_delete"),
    path("message/",views.Messages_view,name="Messages_view"),
    path("project_view/",views.prject_view,name="prject_view"),
     path("delete_message/<int:contact_id>/", views.message_delete, name="message_delete")
]