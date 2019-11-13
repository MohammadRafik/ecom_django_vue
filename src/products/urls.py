from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.BaseLoader.as_view(), name='home'),
]
