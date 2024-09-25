from django.contrib.sessions.backends.base import SessionBase
from kitchenware.models import Product

class CartSession(SessionBase):
    CART_SESSION_ID = 'cart'
    
    
    def __init__(self, session: dict) -> None:
        self.session : dict = session
        self.cart = self.session.get(self.CART_SESSION_ID)
        
        if not self.cart:
            
            self.cart = self.session[self.CART_SESSION_ID] = {}
            
    def __iter__(self): 
        
        product_ids = self.cart.keys()
        
        products = Product.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quanity']
            yield item
            
    def __len__(self):
        return sum(item['quanity'] for item in self.cart.values()) 
    
    def save(self):
        self.session.modified = True
        
    def add(self, product, quanity=1, update_quanity=False):
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {'quanity' : 0, 'price': product.price}
        
        if update_quanity:
            self.cart[product_id]['quanity'] = quanity
        
        else:
            self.cart[product_id]['quanity'] += quanity
        self.save()
    
    def remove(self, product):
        product_id = str(product.id)
        
        if product_id in self.cart:
            if self.cart[product_id]['quanity'] > 1:
                self.cart[product_id]['quanity'] -= 1
            else:
                del self.cart[product_id]
            self.save()
            
    def get_total_price(self):
        return sum(int(item['price']) * int(item['quanity']) for item in self.cart.values())
    
    def clear(self):
        del self.session[self.CART_SESSION_ID]
        self.save()