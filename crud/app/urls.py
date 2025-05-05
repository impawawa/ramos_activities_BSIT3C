from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, RenterViewSet, RentalViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'renters', RenterViewSet)
router.register(r'rentals', RentalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
