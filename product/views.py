from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from .serializers import *


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAllView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAllView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandCreateView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandListAllView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
