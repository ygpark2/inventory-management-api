from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from accounts.permissions import ModelPermissions

from django_filters import DateFromToRangeFilter, DateRangeFilter, DateTimeFilter, FilterSet
from django_filters.rest_framework import DjangoFilterBackend


class OrderPagination(LimitOffsetPagination):
    default_limit = 10


class OrderFilter(FilterSet):
    start_date = DateTimeFilter(field_name='created_at', lookup_expr='gte')
    end_date = DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Order
        fields = ('start_date', 'end_date')


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    permission_classes = [IsAuthenticated, ModelPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        quantity = serializer.validated_data["quantity"]
        product = serializer.validated_data["product"]
        if product.quantity - quantity > 0:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'error': "Out of stock"}, status=status.HTTP_400_BAD_REQUEST)
