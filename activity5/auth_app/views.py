from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']

            if User.objects.filter(username=username).exists():
                return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(
                username=username,
                password=make_password(password)  # \Hash password
            )
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

        except KeyError:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
        
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated"})
