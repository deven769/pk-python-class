from django.contrib import admin

from .models import Category, Product, Testimonials, Cart, CartItem
# Register your models here.
admin.site.register([Category, Product, Testimonials, Cart, CartItem])