from django.urls import path
from .views import (
    posts_detail_view,
    posts_list_view,
    posts_update_view,
)

urlpatterns = [
    path('', posts_list_view),
    path('<str:slug>/', posts_detail_view),
    path('<str:slug>/edit/', posts_update_view),
]