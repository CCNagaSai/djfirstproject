from . import views
from django.urls import path

urlpatterns = [
    path("member/", views.member, name='member'),
    path('member/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
    path('testing/', views.testing, name='testing'),
]