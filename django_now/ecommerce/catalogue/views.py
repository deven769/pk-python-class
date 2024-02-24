from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
	if request.method == 'GET':
		best_seller = Product.objects.filter(is_best_seller = True)
		return render(request, 'client/index.html', {"best_seller": best_seller})