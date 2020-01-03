from django.urls import path
from . import views

#Tempalte urls

app_name= 'basic_app'

urlpatterns= [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login')
]