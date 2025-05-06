from rest_framework import viewsets, permissions
from .models import Car, Renter, Rental
from .serializers import CarSerializer, RenterSerializer, RentalSerializer
from django.utils.decorators import method_decorator
from .utils import rate_limit

@method_decorator(rate_limit(max_requests=5, timeframe=60), name='dispatch')
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]

@method_decorator(rate_limit(max_requests=5, timeframe=60), name='dispatch')
class RenterViewSet(viewsets.ModelViewSet):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer
    permission_classes = [permissions.AllowAny]

@method_decorator(rate_limit(max_requests=5, timeframe=60), name='dispatch')
class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.AllowAny]

