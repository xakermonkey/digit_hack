
from .views import *
from django.urls import path


urlpatterns = [
    path("login", login, name='login'),
    path("recoverpw", recoverpw, name='recoverpw'),
    path("main", main, name='main'),
    path("code_to_text", code_to_text, name='code_to_text'),
    path("products", products, name='products'),
    path("products_details", products_details, name='products_details'),
    path("documentation", documentation, name='documentation'),
]
