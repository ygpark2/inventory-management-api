from rest_framework import routers

from accounts.views import UserViewSet, GroupViewSet
from items.views import ItemViewSet
from orders.views import OrderViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'items', ItemViewSet)
router.register(r'orders', OrderViewSet)
