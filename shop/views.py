import telebot as telebot
from django.contrib import auth
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import telebot
from cart.forms import CartAddProductForm
from shop.models import Product
from shop.forms import *


bot = telebot.TeleBot('1547422587:AAEXIed2UyLcT9m5njy-ZpLe8GXMisU73B8')

def HomeView(request):
    return render(request, 'index.html')

def RoomsView(request):
    return render(request, 'rooms-listing.html')

def GirdView(request):
    return render(request, 'blog-grid.html')

def MenuView(request):
    return render(request, 'menu.html')

def AboutView(request):
    return render(request, 'about.html')

def PriceView(request):
    return render(request, 'pricing-tables.html')

def ShopCartView(request):
    return render(request, 'shop-cart.html')

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


def contactform(request):
    if request.method =='POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            recepients = ['myemail@gmail.com']
            copy = form.cleaned_data['copy']
            if copy:
                recepients.append(sender)

            try:
                send_mail(subject, message, 'pipkamv@gmail.com', recepients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            bot.send_message(1080970215, message)
        return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form, 'username': auth.get_user(request).username})



def thanks(request):
    thanks = 'thanks'
    return render(request, 'thanks.html', {'thanks': thanks})

