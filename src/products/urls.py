from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('/products', views.CategoryView)

app_name = 'products'
urlpatterns = [
    path('', views.BaseLoader.as_view(), name='home'),
    path('api', include(router.urls)),
    # path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
