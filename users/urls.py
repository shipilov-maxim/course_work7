from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users.apps import UsersConfig
from users.views import User_API

router = DefaultRouter()
router.register(r'users', User_API, basename='users')

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
