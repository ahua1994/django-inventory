from django.urls import path
from .views import *

urlpatterns = [
    path("product/all", ProductListAllView.as_view()),
    path("product/create", ProductCreateView.as_view()),
    path("category/all", CategoryListAllView.as_view()),
    path("category/create", CategoryCreateView.as_view()),
    path("brand/all", BrandListAllView.as_view()),
    path("brand/create", BrandCreateView.as_view()),
]
