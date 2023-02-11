from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import User
from .serializers import CustomUserSerializer, GroupSerializer

from django.contrib.auth.models import Group


class UserViewSet(GenericViewSet):
    """
    This is just a placeholder GenericViewSet to show structure of
    serializers.py file and allow adding a ViewSet through the router.
    """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=False, permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
