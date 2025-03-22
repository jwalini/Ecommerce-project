from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('user/<int:id>',views.profile,name='profile'),
]