from django.http import request
from django.shortcuts import redirect


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        urls = [
            '/login/login/',
            '/login/ajaxlogin/'
        ]
        if request.session.get('id') or request.path_info in urls:
            response = self.get_response(request)
            return response
        else:
            return redirect('/login/login/')
