from django.urls import path
from .views import *
app_name = 'dashboard'

urlpatterns = [
	
	path('', dashboard, name = 'dashboard'),
	path('category-list/', categoryList, name = 'category-list'),
	path('category-create/', createCategory, name = 'category-create')
]