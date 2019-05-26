from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register', views.Register.as_view(), name='register'),
    path('login', views.Login.as_view(), name='login'),
    

]
