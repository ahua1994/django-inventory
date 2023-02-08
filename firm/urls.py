from django.urls import path
from .views import *

urlpatterns = [
    path("all/", FirmListAllView.as_view()),
    path("create/", FirmCreateView.as_view())
]
