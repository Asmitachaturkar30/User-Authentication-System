from django.urls import path
from .views import *

urlpatterns=[
    path('home1/',home,name='home1'),
    path('login_page/',login_page,name='login'),
    path('register_page/',register_page,name='register_page'),
    path('delete_page/',delete_page,name='delete_page'),

]