from django.urls import path
from .views import *
app_name = 'dashboard'

urlpatterns = [
	
	path('', dashboard, name = 'dashboard'),
	path('category-list/', categoryList, name = 'category-list'),
	path('category-create/', createCategory, name = 'category-create'),
	path('category-update/<int:pk>/', updateCategory, name = "category-update"),
	path('category-delete/<int:pk>/', deleteCategory, name = "category-delete"),
	path('product-list', ProductList.as_view(), name = 'product-list'),
	path('product-create/', ProductCreate.as_view(), name = 'product-create'),


]