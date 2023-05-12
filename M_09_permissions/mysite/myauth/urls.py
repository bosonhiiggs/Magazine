from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    AboutMeView,
    MyLogoutView,
    RegisterView,
)

app_name = "myauth"

urlpatterns = [
    path(
        "login/", LoginView.as_view(
            template_name='myauth/login.html',
            redirect_authenticated_user=True,
        ),
        name="login"),
    path('register/', RegisterView.as_view(), name='register'),

    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
]
