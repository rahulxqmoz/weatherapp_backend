from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import login
from django.http import JsonResponse
from rest_framework.views import APIView
from google.oauth2 import id_token
from google.auth.transport.requests import Request
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .models import CustomUser
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class WeatherAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, city):
        api_key = settings.WEATHER_API_KEY
        url=f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=10"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({"error": "City not found"}, status=status.HTTP_404_NOT_FOUND)
    


class GoogleLogin(APIView):
    def post(self, request):
        token = request.data.get('token')
        try:
            # Verify the token with Google's servers
            id_info = id_token.verify_oauth2_token(token, Request(), settings.GOOGLE_CLIENT_ID)

            # Extract user information
            email = id_info['email']
            first_name = id_info['given_name']
             

            # Check if user already exists
            user, created = CustomUser.objects.get_or_create(email=email, defaults={
                'username': email.split('@')[0],
                'first_name': first_name,
                'role': 'user',
                
            })

            if not user.is_active:
                return Response({'error': 'User account is inactive.'}, status=status.HTTP_403_FORBIDDEN)


            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token  = AccessToken.for_user(user)

            response_data = {
                "role": user.role,
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                'uidb64': uidb64,
                'access_token': str(token)
            }

            # Return appropriate response
            return Response({
                'is_new_user': created,
                **response_data
            }, status=status.HTTP_200_OK)

        except ValueError:
            # Invalid token
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Ensure the user is an admin
        if request.user.role != 'admin':
            return Response({'error': 'Permission denied, admin access required.'}, status=status.HTTP_403_FORBIDDEN)

        users = CustomUser.objects.all()
        users_data = [
            {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'is_active': user.is_active,
            }
            for user in users
        ]
        return Response(users_data, status=status.HTTP_200_OK)
    

class BlockUnblockUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # Ensure the user is an admin
        if request.user.role != 'admin':
            return Response({'error': 'Permission denied, admin access required.'}, status=status.HTTP_403_FORBIDDEN)

        # Get the action from the request data
        action = request.data.get('action')

        if action not in ['block', 'unblock']:
            return Response({'error': "Invalid action. Use 'block' or 'unblock'."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(id=user_id)
            
            # Block or unblock the user based on the action
            if action == 'block':
                user.is_active = False
                message = 'User has been blocked.'
            elif action == 'unblock':
                user.is_active = True
                message = 'User has been unblocked.'
            
            user.save()
            return Response({'message': message}, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
