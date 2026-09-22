# accounts/permissions.py
from functools import wraps
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login


def group_required(*group_names):
    """
    Anonymous → redirect to login.
    Logged in but not in any of these groups → 403.
    Superusers always pass.
    """
    def decorator(view):
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            user = request.user

            if not user.is_authenticated:
                return redirect_to_login(request.get_full_path())

            if user.is_superuser or user.groups.filter(name__in=group_names).exists():
                return view(request, *args, **kwargs)

            raise PermissionDenied
        return wrapper
    return decorator