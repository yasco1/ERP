from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class ReadOnly (BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS)


# HR Permissions
class isAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False    
    
class is_hr_all(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return bool(request.user.is_HR)

class is_hr_or_pr(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return bool(request.user.is_HR) or bool(request.user.is_PR)

class is_hr_except_get(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user and request.user.is_authenticated:
            return True
        elif request.user and request.user.is_authenticated:
            return bool(request.user.is_HR)
        else:
            return False
