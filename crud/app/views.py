from rest_framework import viewsets, permissions
from .models import Car, Renter, Rental
from .serializers import CarSerializer, RenterSerializer, RentalSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]  # Disable authentication

class RenterViewSet(viewsets.ModelViewSet):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer
    permission_classes = [permissions.AllowAny]  # Disable authentication

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.AllowAny]  # Disable authentication
