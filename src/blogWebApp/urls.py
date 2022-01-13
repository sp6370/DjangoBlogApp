from django.contrib import admin
from django.urls import path, include
from .views import (
    register_request,
    login_request,
    logout_request
)

from posts.views import (
    posts_list_view,
    posts_create_view,
)

urlpatterns = [
    path('', posts_list_view),
    path('blog-new/', posts_create_view),
    path('blog/', include('posts.urls')),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name= "logout"),
    path('admin/', admin.site.urls)
]







    