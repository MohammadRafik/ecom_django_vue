"""djangobase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from products import views as productviews


router = routers.DefaultRouter()
router.register('categories', productviews.CategoryView)
router.register('suppliers', productviews.SupplierView)
router.register('products', productviews.ProductView)
router.register('productimages', productviews.ProductImageView)

#including the models of a different app here to add them to the api easily
from cart import views as cartviews
router.register('cart', cartviews.CartViewSet)
router.register('cartitem', cartviews.CartItemViewSet)
router.register('checkoutdetails', cartviews.CheckoutDetailsViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('api/', include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
