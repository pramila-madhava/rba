# # middleware.py

# from django.utils.deprecation import MiddlewareMixin

# class GetClientIPMiddleware(MiddlewareMixin):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         request.client_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
#         response = self.get_response(request)
#         return response
# middleware.py

class GetClientIPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.client_ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        response = self.get_response(request)
        return response
