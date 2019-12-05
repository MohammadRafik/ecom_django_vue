from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.CategoryView)
router.register('suppliers', views.SupplierView)
router.register('products', views.ProductView)
router.register('productimages', views.ProductImageView)

app_name = 'products'
urlpatterns = [
    path('', views.BaseLoader.as_view(), name='home'),
    path('category/search/<filter>/', views.BaseLoader.as_view(), name='filter'),
    path('api/', include(router.urls)),
    path('api/session/', views.SessionAccess.as_view(), name='xd123'),



]
