
from .views import *
from django.urls import path


urlpatterns = [
    path("login", login, name='login'),
    path("recoverpw", recoverpw, name='recoverpw'),
    path("main", main, name='main'),
    path("employees", employees, name='employees'),
    path("products", products, name='products'),
    path("nomenclature", nomenclature, name='nomenclature'),
]
