from django.urls import path
from .views import (
    AuthLoginProxyView,
    AuthSessionStatusProxyView,
    AuthLogoutProxyView,
)

urlpatterns = [
    path('auth/login/', AuthLoginProxyView.as_view()),
    path('auth/register/', AuthLoginProxyView.as_view()),
    path('auth/session-status/', AuthSessionStatusProxyView.as_view()),
    path('auth/logout/', AuthLogoutProxyView.as_view()),
]
