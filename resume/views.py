from rest_framework import viewsets

from resume.permissions import IsOwnerOrReadOnly
from resume.models import Resume
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from resume.serializers import UserLoginSerializer, ResumeSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from http import HTTPStatus


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @method_decorator(login_required)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class LoginAPIView(APIView):
    def post(self, request):
        user = authenticate(request, **request.data)
        if user is not None:
            login(request, user)
            return Response(
                UserLoginSerializer(user).data,
                status=HTTPStatus.OK
            )
        return Response(status=HTTPStatus.BAD_REQUEST)


class LogoutAPIView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
        return Response(status=HTTPStatus.OK)
