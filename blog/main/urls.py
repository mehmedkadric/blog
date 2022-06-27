from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("/", views.homepage, name="homepage"),
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("register", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("logout", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("login", views.login_request, name="login"),
    path("about/", views.about_us, name="about"),
    path("about", views.about_us, name="about"),
    path("profile/", views.profile, name="profile"),
    path("profile", views.profile, name="profile"),
    path("landing/", views.landing_page, name="landing"),
    path("landing", views.landing_page, name="landing"),
    path("<single_slug>", views.single_slug, name="single_slug"),

]
