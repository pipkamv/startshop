from django.urls import path
from .views import *
app_name = 'shop'

urlpatterns = [
    path('', HomeView, name='home'),
    path('rooms/', RoomsView, name='rooms' ),
    path('gird/', GirdView, name='gird'),
    path('menu/', MenuView, name='menu'),
    path('about/', AboutView, name='about'),
    path('price/', PriceView, name='price'),
    path('shopcart/', ShopCartView, name='shop-cart'),
    # path('contact/', ContactView, name='contact'),
    path('contact/', contactform, name='contact'),
    path('thanks/', thanks, name='thanks'),
    # path('contact_form', ContactForm, 'contact_form'),

]



