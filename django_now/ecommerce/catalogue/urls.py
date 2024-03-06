from django.urls import path
from .views import index, productDetail,addToCart
app_name = 'catalogue'

urlpatterns = [
	path('', index, name = 'index'),
	path('product/<int:pk>/', productDetail, name = 'product-detail'),
	path('add-to-cart', addToCart, name = 'add-to-cart')
]

