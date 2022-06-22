class SimpleMiddleWare(object):
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        # print('SimpleMiddleWare initialized: ', type(get_response), '   ', get_response)
    
    def __call__(self, request,  *args, **kwds):
        # print('SimpleMiddleWare called befor view ', type(request), '   ', request, '  ', request.headers)
        request = self.add_request_header(request)
        #print(request.headers)
        # print(request.META)
        response = self.get_response(request)
        
        response = self.add_reponse_header(response)
        
        # print('This code called after executing the view: ')
        # print(response, '   ', type(response), '   ', response.headers)
        # print(response.headers)
        return response
    
    def add_request_header(self, request):
        # This function shows how we can change every view behavior by CustomMiddlewares
        request.META['custom header'] = 'custom REQUEST data'
        return request
    
    def add_reponse_header(self, response):
        # This function shows how we can change every view behavior by CustomMiddlewares
        response.headers['Custom_header'] = 'custom RESPONSE data'
        return response
