from django.contrib import admin
from django.urls import path
from .views import (
    register_request,
    login_request,
    logout_request
)

urlpatterns = [
    path('', login_request, name="login"),
    path('admin/', admin.site.urls),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name= "logout"),
]