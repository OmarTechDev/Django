from django.http import JsonResponse
from django.urls import resolve
from rest_framework_simplejwt.authentication import JWTAuthentication

class RoleBasedPermissionMiddleware:
    """
    Middleware  Validations to accessibility for some urls.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.public_routes = [
            '/',              # Página de inicio
            '/favicon.ico',
            '/admin',
            '/admin/',
            '/admin/login/?next=/admin/'
        ]
        self.role_permissions = {
            #'/estate/': ['admin', 'agent'],
        }

    def __call__(self, request):
        print("path de entrada",request.path)
        if request.path.startswith('/admin/') or request.path in self.public_routes or request.path.startswith('/api/'):
            return self.get_response(request)

        if request.path in self.public_routes:
            return self.get_response(request)

        try:
            user_auth = JWTAuthentication()
            user, token = user_auth.authenticate(request)

            user_role = token.get('role')

            if not user_role:
                return JsonResponse({'error': 'Role not found in token'}, status=403)

            from django.urls import resolve
            resolver = resolve(request.path_info)
            view_name = resolver.view_name

            allowed_views = self.role_permissions.get(user_role, [])
            if view_name not in allowed_views:
                return JsonResponse({'error': 'Permission denied'}, status=403)

        except Exception:
            return JsonResponse({'error': 'Authentication required'}, status=401)

        response = self.get_response(request)
        return response
