from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('testVue', views.testing_vue, name='testingvue'),
    path('testbase', views.test_base, name='testbase'),
    # path('', views.index, name='index'),
    path('home', views.test_base, name='home'),
]