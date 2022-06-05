
from .views import *
from django.urls import path


urlpatterns = [
    path("login", login, name='login'),
    path("recoverpw", recoverpw, name='recoverpw'),
    path("main", main, name='main'),
    path("code_to_text", code_to_text, name='code_to_text'),
    path("products", products, name='products'),
    path("get_descriptoin", get_descriptoin),
    path("products_details/accept_left", accept_left),
    path("products_details/accept_right", accept_right),
    path("products_details/<int:pk>", products_details, name='products_details'),
    path("documentation", documentation, name='documentation'),
    path("post_data", getDT.as_view()),
    path("new_dt", new_dt),
]
