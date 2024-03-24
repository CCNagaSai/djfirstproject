from . import views
from django.urls import path

urlpatterns = [
    path("member/", views.member, name='member'),
]