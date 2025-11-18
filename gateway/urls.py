from django.urls import path
from .views import (
    AuthLoginProxyView,
    AuthSessionStatusProxyView,
    AuthLogoutProxyView,
    AuthRegisterProxyView
)

urlpatterns = [
    path('auth/login/', AuthLoginProxyView.as_view()),
    path('auth/register/', AuthRegisterProxyView.as_view()),
    path('auth/session-status/', AuthSessionStatusProxyView.as_view()),
    path('auth/logout/', AuthLogoutProxyView.as_view()),
]
