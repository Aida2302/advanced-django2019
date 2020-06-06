from rest_framework.permissions import IsAuthenticated


class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_super_admin or request.user.is_store_admin
