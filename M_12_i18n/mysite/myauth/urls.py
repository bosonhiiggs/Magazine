from django.contrib.auth.views import LoginView
from django.urls import path


from .views import (
    get_cookie_view,
    set_cookie_view,
    set_session_view,
    get_session_view,

    MyLogoutView,
    AboutMeView,
    UserDetailsView,
    UpdateProfileImage,
    UsersListView,
    UpdateAboutMeView,
    RegisterView,
    FooBarView,
    HelloView,
)

app_name = "myauth"

urlpatterns = [
    # path("login/", login_view, name="login"),
    path(
        "login/",
        LoginView.as_view(
            template_name="myauth/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path('hello/', HelloView.as_view(), name='hello'),
    # path("logout/", logout_view, name="logout"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),

    path('users/', UsersListView.as_view(), name="users"),
    path('users/<int:pk>/', UserDetailsView.as_view(), name="user_me"),
    path('users/<int:pk>/update/', UpdateProfileImage.as_view(), name="update_img"),
    path("about-me/", AboutMeView.as_view(), name="about_me"),
    path("about-me/<int:pk>/update", UpdateAboutMeView.as_view(), name="user_update"),

    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("cookie/set/", set_cookie_view, name="cookie-set"),

    path("session/set/", set_session_view, name="session-set"),
    path("session/get/", get_session_view, name="session-get"),

    path("foo-bar/", FooBarView.as_view(), name="foo-bar"),
]
