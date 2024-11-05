from django.contrib import admin
from home.models import product, Cart, cart_item

# Register your models here.
admin.site.register(product)
admin.site.register(Cart)
admin.site.register(cart_item)