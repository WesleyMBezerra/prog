from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def admin_only(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.email in settings.ADMIN_EMAILS:
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return wrapper
