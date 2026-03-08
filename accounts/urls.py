from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import SignupAPIView, SessionLogoutAPIView
from .views_page import LoginPageView, SignupPageView

urlpatterns = [
    # API
    path("api/signup/", SignupAPIView.as_view(), name="api-signup"),
    path("api/login/", TokenObtainPairView.as_view(), name="jwt-login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("api/logout/", SessionLogoutAPIView.as_view(), name="api-logout"),
    # Pages
    path("signup-page/", SignupPageView.as_view(), name="page-signup"),
    path("login/", LoginPageView.as_view(), name="page-login"),
    path(
        "",
        lambda request: __import__("django.shortcuts", fromlist=["redirect"]).redirect(
            "page-login"
        ),
        name="root",
    ),
]
