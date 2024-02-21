from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
	if request.method == 'GET':
		products = Product.objects.all()

		print(products)
		return render(request, 'client/index.html', {"products": products})