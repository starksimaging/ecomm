from decimal import Decimal
from django.conf import settings
from store_app.models import Shoe

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESION_ID] = {}
            self.cart = cart

def add(self, shoe, quantity=1, update_quantity=False):
    shoe_id = str(shoe.id)
    if shoe_id not in self.cart:
        self.cart[shoe_id] = {'quantity': 0, 'price': str(shoe.price)}
        if update_quantity:
            self.cart[shoe_id]['quantity']= quantity
        else:
            self.cart[shoe_id]['quantity'] += quantity
        self.save()

def save(self):
    self.session[settings.CART_SESSION_ID] = self.cart
    self.session.modifies = True

def remove(self, shoe):
    shoe_id = str(shoe .id)
    if shoe_id in self.cart:
        del self.cart[shoe_id]
        self.save()


def __inter__(self):
    shoe_ids = self.cart.keys()
    shoes = Shoe.objects.filter(id__in=shoe_ids)
    for shoe in shoes:
        self.cart[str(shoe.id)]['shoe'] = shoe
    for item in self.cart.values():
        item['price'] = Decimal(item['price'])
        item['total_price'] = item['price'] * item['quantity']
        yield item

def __len__(self):
    return sum(item['quintity'] for item in self.cart.values())


def get_total_price(self):
    return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


def clear(self):
    del self.session[settings.CART_SESSION_ID]
    self.session.modified = True