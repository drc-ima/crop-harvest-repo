from django.urls import path

from . views import *

app_name = "user"

# user:signup
urlpatterns = [
    path("signup/", signup, name="signup"),
    path("dashboard/", dashboard, name="dashboard")
]
