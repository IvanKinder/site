# from wsgiref.simple_server import make_server
import quopri
from requests_handler import GetRequests, PostRequests
from urls import routes, fronts
from views import PageNotFound404


class Framework:
    def __init__(self, routes_obj, front_obj):
        self.routes_list = routes_obj
        self.front_list = front_obj

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        request = {}

        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print('Пришел get-запрос с параметрами: ', request_params)
        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print('Пришел post-запрос: ', Framework.decode_value(data))

        if path[-1] != '/':
            path = path + '/'
        if path in self.routes_list:
            view = self.routes_list[path]
        else:
            view = PageNotFound404()

        # request = {}
        for front in self.front_list:
            front(request)

        code, body = view(request)
        start_response(code, [('Content-type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data: dict):
        new_data = {}
        for key, value in data.items():
            val = bytes(value.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[key] = val_decode_str
        return new_data


application = Framework(routes, fronts)




