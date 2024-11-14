from . import views
from django.urls import path


app_name="dashboard"

urlpatterns=[

    path("dashboard/",views.dashboard_view,name="dashboard_view"),
    path("update/<proj_id>/",views.project_update,name="project_update")
]