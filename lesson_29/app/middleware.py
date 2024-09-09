def simple_middleware(get_response):

    def middleware(request):

        request.my_custom_attr_1 = "Custom attribute 1"
        response = get_response(request)

        return response
    
    return middleware

    


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.my_custom_attr_2 = "Custom attribute 2"
        response = self.get_response(request)
        return response
    


def greeting_message(request):
    return {'greeting_message': 'Hello my brooooooooo'}


'django_middleware_bootstrap_templatetags'