from django.urls import path
from . import views

app_name = 'pageloader'
urlpatterns = [
    path('', views.BaseLoader.as_view(), name='home'),
]
