class Handler:
    methods = set()
    def __init__(self, methods=("GET",)):
        self.methods = methods
    
    def __call__(self, func, *args, **kwargs):
        type_methods = {
            "GET": self.get,
            "POST": self.post,
        }
        def wrapper(req: dict):
            if req['methods'] not in self.methods:
                raise f'Данная страница не принимает запросы с методами: {req["methods"]}'
            
            return type_methods[req['methods']](func, req, *args, **kwargs)
        
        return wrapper
    def get(self, func, request, *args, **kwargs):
        return func(request, *args, **kwargs)
    
    def post(self, func, request, *args, **kwargs):
        return func(request, *args, **kwargs)
    

@Handler(methods=("GET"))
def get_page(req: dict):
    return 'Hello world'

print(get_page({
    'methods': 'GET'
}))

class Power:
    exp: float = 0
    
    def __init__(self, exp: float):
        self.exp = exp
        
    def __call__(self, n: float):
        return n ** self.exp
    
class Repeat:
    quantity: int = 1
    
    def __init__(self, quantity: int):
        self.quantity = quantity
        
    def __call__(self, func):
        
        def wrapper():
            for _ in range(self.quantity):
                func()
        
        return wrapper
