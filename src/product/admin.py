from django.contrib import admin
from .models import Category, Product, UserBasket, Basket

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserBasket)
admin.site.register(Basket)
