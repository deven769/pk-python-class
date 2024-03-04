from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Testimonials
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
	if request.method == 'GET':
		product = Product.objects.get(id = pk)
		return render(request, 'client/productdetail.html', {'product':product})


@login_required(login_url = 'accounts/login')
def addToCart(request):

	if request.method == 'POST':
		product_id = request.POST.get('product_id')
		product = get_object_or_404(Product, id = product_id)
		quanity = request.post.get('quanity')

		if Cart.objects.filter(user = request.user).exists():
			cart = get_object_or_404(user = request.user)
		else:
			Cart.objects.create(user = request.user)
			cart = get_object_or_404(user = request.user)
		CartItem.objects.create(cart = cart, quanity = quanity, product = product)

		pass 

