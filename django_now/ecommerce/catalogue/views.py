from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Testimonials, Category, Cart, CartItem
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
	if request.method == 'GET':
		best_seller = Product.objects.filter(is_best_seller = True)
		our_organic_products = Product.objects.order_by('?')[0:4]
		testimonials = Testimonials.objects.all()
		print(testimonials)
		return render(request, 'client/index.html', {"best_seller": best_seller, "our_organic_products":our_organic_products, 'testimonials':testimonials})


def productDetail(request, pk):
    if request.method =='GET':
        specific_product = get_object_or_404(Product, id = pk)
        category = Category.objects.all()
        featured_products = Product.objects.filter(is_featured=True)

        return render(request, 'client/productdetail.html', {"specific_product":specific_product, "category":category,"featured_products":featured_products})

@login_required(login_url = 'accounts/login')
def addToCart(request):
	if request.method == 'GET':
		cart_items =  	CartItem.objects.filter(cart__user = request.user)
		cart_total = Cart.get_total(request.user)
		print(cart_total,'======================')
		return render(request, 'client/cart.html', {'cart_items':cart_items, 'cart_total':cart_total})

	if request.method == 'POST':
		product_id = request.POST.get('product_id')
		product = get_object_or_404(Product, id = product_id)
		quanity = request.POST.get('quanity')

		if Cart.objects.filter(user = request.user).exists():
			cart = get_object_or_404(Cart,user = request.user)
		else:
			Cart.objects.create(user = request.user)
			cart = get_object_or_404(Cart,user = request.user)
		if CartItem.objects.filter(cart__user = request.user, product__id = product.id).exists():
			item = CartItem.objects.get(cart__user = request.user, product__id = product.id)
			db_quanity = int(quanity) + item.quanity
			item.quanity = db_quanity
			item.save()
		else:
			CartItem.objects.create(cart = cart, quanity = quanity, product = product)

		return redirect('catalogue:product-detail', pk = product_id)

def updateCartItem(request, pk):
	if request.method == 'POST':
		quanity = request.POST.get('quanity')
		item = get_object_or_404(Cart, id = pk)
		item.quanity = quanity
		item.save()
		return redirect('catalogue:add-to-cart')

		# CartItem.objects.filter(id = pk).update(quanity = quanity)

