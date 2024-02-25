from django.shortcuts import render
from .models import Product, Testimonials

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
