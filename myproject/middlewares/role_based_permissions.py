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
            '/',
            '/favicon.ico',
            '/admin',
            '/admin/',
            '/admin/login/?next=/admin/',
            '/users/login/'
        ]
        self.role_permissions = {
            'user': [
                'list_users',
                'register_user'
            ]
        }

    def __call__(self, request):

        # user_auth = JWTAuthentication()
        # tokenA = user_auth.authenticate(request)
        # print("TryA", user_auth)
        # print("TryB", tokenA)

        if request.path.startswith('/admin/') or request.path in self.public_routes:
            print("HERE-----------------------------------------------")
            return self.get_response(request)

        try:
            user_auth = JWTAuthentication()
            user, token = user_auth.authenticate(request)
            print("Try", token)
            user_role = token.get('role')
            print("Your ROLE--------------------------", user_role)

            if not user_role:
                return JsonResponse({'error': 'Role not found in token'}, status=403)
            try:
                resolver = resolve(request.path_info)
                print('Resolver:', resolver)
                view_name = resolver.view_name
                print('View Name:', view_name)
            except Exception as e:
                print('Error resolving the view:', str(e))
                return JsonResponse({'error': 'Error resolving the view'}, status=500)

            allowed_views = self.role_permissions.get(user_role, [])
            print('Allowed Views', allowed_views)
            if view_name not in allowed_views:
                return JsonResponse({'error': 'Permission denied'}, status=403)
        except Exception:
            return JsonResponse({'error': 'Authentication required'}, status=401)

        response = self.get_response(request)
        return response
