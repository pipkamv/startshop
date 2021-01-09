from django.urls import path
from .views import *
app_name = 'cart'


urlpatterns =[
    path('cart_detail', cart_detail, name='cart_detail'),
    path('cart_views', cart_add, name='cart_add'),
    path('cart_remove', cart_remove, name='cart_remove'),
]




