from django.contrib import admin

from .models import Category, Product, Testimonials, Cart, CartItem
# Register your models here.
admin.site.register([Category, Testimonials, Cart, CartItem])




admin.site.site_title = "Ecommerce site"
admin.site.name = "Ecommerce by Deven"
admin.site.index_title = "Welcome to the Ecommerce Admin Dashboard"
admin.site.site_header = "Ecommerce Administration"
admin.site.site_footer = "© 2024 Ecommerce by Deven. All rights reserved."




class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity','is_featured', 'is_best_seller')
    search_fields = ('name','price')
    ordering = ('name',) 
    # list_display_links = ('slug',)
    list_editable = ('quantity',)
    list_per_page = (2)
    
admin.site.register(Product, ProductAdmin)

