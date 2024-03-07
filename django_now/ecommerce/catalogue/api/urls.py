from django.urls import path
from .views import *
app_name = 'catalogue_api'

urlpatterns = [
	path('category-list/', CategoryListView.as_view(), name = 'category-list'),
	path('category-update/<int:pk>/', CategoryUpdateView.as_view(), name = 'category-update'),

	path('product-list/', ProductListView.as_view(), name = 'product-list'),
	path('product-update/<int:pk>/', ProductUpdateView.as_view(), name = 'product-update'),
]

