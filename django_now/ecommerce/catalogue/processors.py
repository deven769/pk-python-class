from catalogue.models import Cart, Category

def global_variable(request):
	context = {}
	if request.user.is_authenticated:
		context['cart_count'] = Cart.get_Total_count(request.user)
	context['nav_category'] = Category.objects.all()[:4]
	return context