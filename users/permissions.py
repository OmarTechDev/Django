# from rest_framework.permissions import BasePermission

# class IsAdminRole(BasePermission):
#     """
#     Permite acceso solo a usuarios con el rol 'admin'.
#     """
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'admin'


# class IsAgentRole(BasePermission):
#     """
#     Permite acceso solo a usuarios con el rol 'agent'.
#     """
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'agent'
