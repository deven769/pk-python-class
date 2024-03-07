from rest_framework.generics import (ListAPIView,
	ListCreateAPIView,
	UpdateAPIView,
	RetrieveUpdateAPIView,
	RetrieveUpdateDestroyAPIView)
from .serializers import CategorySerializers,ProductSerializers
from catalogue.models import Category, Product
from .permissions import HasAdminPermission


class CategoryListView(ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializers
	permission_classes = [HasAdminPermission]


class CategoryUpdateView(RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializers
	permission_classes = [HasAdminPermission]


class ProductListView(ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializers
	permission_classes = [HasAdminPermission]


class ProductUpdateView(RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializers
	permission_classes = [HasAdminPermission]




