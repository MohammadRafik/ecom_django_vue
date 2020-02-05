from django.urls import path, include
from . import views
from rest_framework import routers





app_name = 'products'
urlpatterns = [
    path('', views.BaseLoader.as_view(), name='home'),
    path('category/search/<filter>/', views.BaseLoader.as_view(), name='filter'),
    path('category/search/$', views.product_search, name='product_search'),
    path('api/session/', views.SessionAccess.as_view(), name='xd123'),
    path('api/get_url/', views.get_url, name='get_url_from_django'),
    path('product/<product_id>/', views.product_page, name='product_page'),

]
