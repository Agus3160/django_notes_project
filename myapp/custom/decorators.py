from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

def kick_auth_auth_users(redirect_to):
    """
    Decorator for views that checks if the user is logged in, redirecting
    to other page if necessary.
    """

    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper
