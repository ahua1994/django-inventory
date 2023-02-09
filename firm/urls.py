from django.urls import path
from .views import *

urlpatterns = [
    path("all/", FirmListAllView.as_view()),
    path("create/", FirmCreateView.as_view()),
    path("purchases/all/", PurchasesListAllView.as_view()),
    path("purchases/<int:pk>/", PurchasesUpdateView.as_view()),
    path("purchases/buy/", PurchasesCreateView.as_view()),
    path("sales/all/", SalesListAllView.as_view()),
    path("sales/sell/", SalesCreateView.as_view()),
]
