from django.shortcuts import redirect
from django.urls import reverse, resolve

from .views import SearchView


class SearchMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if 'search' in request.GET:
            search = request.GET.get('search').strip()
            if search == '':
                return redirect(reverse('statesng:home:index'))
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        resolved_url = resolve(request.path)
        if resolved_url.func.__name__ == 'SearchView' and 'search' not in request.GET:
            """Will implement later if /search/ is directly accessed without query"""
        try:
            search = request.GET['search']
        except KeyError:
            return None
