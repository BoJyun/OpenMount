from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_index,name='get_index'),
    path('signup',views.signup,name='signup'),
]
