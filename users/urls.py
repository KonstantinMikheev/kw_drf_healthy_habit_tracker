from django.urls import path

from habits.views import HabitsPublicListAPIView
from users.apps import UsersConfig
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_framework.permissions import AllowAny

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login",),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh",),
    path( "public_habits/", HabitsPublicListAPIView.as_view(), name="public-habits")
]

urlpatterns += router.urls
