from django.urls import include, path
from rest_framework import routers

from . import views
from .views import LoginAPIView, LogoutAPIView

router = routers.DefaultRouter()
router.register('resume', views.ResumeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
]
