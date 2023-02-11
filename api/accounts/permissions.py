import copy
from django.contrib.auth.models import Group
from rest_framework.permissions import DjangoModelPermissions, BasePermission, SAFE_METHODS


class ModelPermissions(DjangoModelPermissions):

    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map) # you need deepcopy when you inherit a dictionary type 


class HasGroupPermission(BasePermission):
    def _is_in_group(user, group_name):
        try:
            return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
        except Group.DoesNotExist:
            return False

    def has_permission(self, request, view):
        required_groups = view.permission_groups.get(view.action)
        if required_groups is None:
            return False
        elif "_Public" in required_groups:
            return True
        else:
            return any(
                [
                    _is_in_group(request.user, group_name)
                    for group_name in required_groups
                ]
            )


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
