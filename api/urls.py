
from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, ProductImageViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'product-images', ProductImageViewSet, basename='product-image')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include("djoser.urls")),
    path('api/', include("users.urls")),
]
