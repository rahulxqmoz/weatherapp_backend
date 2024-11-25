from django.urls import path
from .views import GoogleLogin,WeatherAPIView,UserListView,BlockUnblockUserView

urlpatterns = [
    path('weather/<str:city>/', WeatherAPIView.as_view(), name='weather'),
    path('auth/google/', GoogleLogin.as_view(), name='google-login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/block_unblock/<int:user_id>/', BlockUnblockUserView.as_view(), name='block-user'),
    
]
