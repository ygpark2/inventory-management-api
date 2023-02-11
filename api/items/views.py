from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Item
from .serializers import ItemSerializer
from accounts.permissions import ModelPermissions


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, ModelPermissions]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
