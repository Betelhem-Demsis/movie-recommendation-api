from rest_framework import status, generics
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes=[AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  
        return Response({'user': user.id}, status=status.HTTP_201_CREATED)
        

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer  
    permission_classes = [AllowAny]  

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user'] 
            token, created = Token.objects.get_or_create(user=user) 
            return Response({'token': token.key}, status=status.HTTP_200_OK)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user) 
            token.delete()  
            return Response({"message": "Successfully logged out"}, status=200)  
        except Token.DoesNotExist:
            return Response({"error": "Token not found"}, status=400)  


