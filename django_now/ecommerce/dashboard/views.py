from django.shortcuts import render
from catalogue.models import Category, Product
from .forms import CategoryForm, ProductForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

@user_passes_test(lambda u:u.is_staff)
def dashboard(request):
	if request.method == 'GET':
		return render(request, 'dashboard/dashboard.html')


@user_passes_test(lambda u:u.is_staff)
def categoryList(request):
	if request.method == 'GET':
		category = Category.objects.all()
		return render(request, 'dashboard/category-list.html', {'category':category})

@user_passes_test(lambda u:u.is_staff)
def createCategory(request):
	if request.method == 'GET':
		form = CategoryForm()
		return render(request, 'dashboard/category-create.html', {'form':form})
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dashboard:category-list')
		return render(request, 'dashboard/category-create.html', {'form':form})

@user_passes_test(lambda u:u.is_staff)
def updateCategory(request, pk):
    category = get_object_or_404(Category, id = pk)
    if request.method == "GET":
        form = CategoryForm(instance=category)
        return render(request, "dashboard/category-update.html",{"category":category, 'form':form})
    
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
        	data = form.cleaned_data
        	# Category.objects.filter(id = category.id).update(name = data['nmae'], display_order = data['display_order']) 
        	form.save()
        	return redirect("dashboard:category-list")
        return render(request, "dashboard/category-update.html", {"category":category, "form":form})
    


@user_passes_test(lambda u:u.is_staff)
def deleteCategory(request, pk):
	category = get_object_or_404(Category,id = pk)
	category.delete()
	return redirect('dashboard:category-list')



class ProductList(UserPassesTestMixin, ListView):
	model = Product
	template_name = 'dashboard/product-list.html'
	context_object_name = 'products'

	def test_func(self):
		return self.request.user.is_staff or self.request.user.is_superuser
    


class ProductCreate(UserPassesTestMixin, CreateView):
    form_class = ProductForm
    template_name = 'dashboard/product-create.html'
    success_url = reverse_lazy('dashboard:product-list')
    





