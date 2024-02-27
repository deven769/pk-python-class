from django.shortcuts import render
from catalogue.models import Category
from .forms import CategoryForm
from django.shortcuts import redirect
# Create your views here.


def dashboard(request):
	if request.method == 'GET':
		return render(request, 'dashboard/dashboard.html')



def categoryList(request):
	if request.method == 'GET':
		category = Category.objects.all()
		return render(request, 'dashboard/category-list.html', {'category':category})

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

