from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.CategoryView)
router.register('suppliers', views.SupplierView)
router.register('products', views.ProductView)
router.register('productimages', views.ProductImageView)
#including the models of a different app here to add them to the api easily
from cart import views as cartviews
router.register('cart', cartviews.CartViewSet)
router.register('cartitem', cartviews.CartItemViewSet)






app_name = 'products'
urlpatterns = [
    path('', views.BaseLoader.as_view(), name='home'),
    path('category/search/<filter>/', views.BaseLoader.as_view(), name='filter'),
    path('category/search/$', views.product_search, name='product_search'),
    path('api/', include(router.urls)),
    # path('api/api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/session/', views.SessionAccess.as_view(), name='xd123'),
    path('product/<product_id>/', views.product_page, name='product_page'),


]
