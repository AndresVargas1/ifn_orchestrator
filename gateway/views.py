import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AuthLoginProxyView(APIView):
    def post(self, request):
        url = settings.AUTH_SERVICE_BASE_URL + "login/"
        try:
            resp = requests.post(url, json=request.data, timeout=10)
        except requests.RequestException:
            return Response(
                {"error": "Servicio de autenticación no disponible"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        try:
            data = resp.json()
        except ValueError:
            data = {"error": "Respuesta inválida del servicio de autenticación"}

        return Response(data, status=resp.status_code)


class AuthSessionStatusProxyView(APIView):
    def post(self, request):
        url = settings.AUTH_SERVICE_BASE_URL + "session-status/"
        try:
            resp = requests.post(url, json=request.data, timeout=10)
        except requests.RequestException:
            return Response(
                {"error": "Servicio de autenticación no disponible"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        try:
            data = resp.json()
        except ValueError:
            data = {"error": "Respuesta inválida del servicio de autenticación"}

        return Response(data, status=resp.status_code)


class AuthLogoutProxyView(APIView):
    def post(self, request):
        url = settings.AUTH_SERVICE_BASE_URL + "logout/"
        try:
            resp = requests.post(url, json=request.data, timeout=10)
        except requests.RequestException:
            return Response(
                {"error": "Servicio de autenticación no disponible"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        try:
            data = resp.json()
        except ValueError:
            data = {"error": "Respuesta inválida del servicio de autenticación"}

        return Response(data, status=resp.status_code)
