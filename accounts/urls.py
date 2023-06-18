from django.urls import path
from .views import (
    JWTTokenObtainView,
    JWTTokenRefreshView,
    UpdatePasswordAPIView,
    LogoutAPIView  
)
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("login/", XERPTokenObtainPairView.as_view())
# router.register("auth/refresh/", XERPTokenRefreshPairView.as_view())
# router.register("logout/", Logout.as_view())


urlpatterns = [
    path("login/", JWTTokenObtainView.as_view()),
    path("refresh/", JWTTokenRefreshView.as_view()),
    path("update_password/<str:uuid>", UpdatePasswordAPIView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
]
