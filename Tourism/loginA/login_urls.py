from django.urls import path
from loginA.views import LoginView, loginAuth, SignupView, LogoutView

urlpatterns = [
    path("", LoginView, name="login"),
    path("auth", loginAuth, name="loginAuth"),
    path("page", SignupView, name="signup"),
    path("logout", LogoutView, name="logout"),
]
