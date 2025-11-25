from rest_framework import routers
from django.urls import path,include
from .views import CustomerViewSet, RestaurantViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet, OrderTrackingViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router=routers.DefaultRouter()
router.register(r'customers',CustomerViewSet)
router.register(r'restaurants',RestaurantViewSet)
router.register(r'products',ProductViewSet)
router.register(r'orders',OrderViewSet)
router.register(r'orderitems',OrderItemViewSet)
router.register(r'ordertrackings',OrderTrackingViewSet)



urlpatterns = [
    path('', include(router.urls)),
]