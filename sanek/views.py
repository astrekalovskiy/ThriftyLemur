from django.shortcuts import render
from django.http import Http404
from django.template import loader

from .models import Store
from .models import Product
# Create your views here.

def index(request):
    try:
        request
    except Product.DoesNotExist:
        raise Http404("Страница не найдена")
    return render(request, 'sanek/index.html', {})

#def urot(request):
#    return HttpResponse("Витя!!"+"<p><img src='https://preview.ibb.co/jRad3U/0_E649_C42_0_E51_4_F10_B8_D2_E7_B96_EBA8_D2_E.jpg' alt='ВИТЬКА ТИТЬКА'></p>")

def productsAll(request):
    try:
        products = Product.objects.all()
        stores = Store.objects.all()
    except Product.DoesNotExist:
        raise Http404("Продукты не найдены")
    return render(request, 'sanek/products.html', {
        'products': products,
        'stores': stores,
        })

def storesAll(request):
    try:
        stores = Store.objects.all()
    except Product.DoesNotExist:
        raise Http404("Магазины не найдены")
    return render(request, 'sanek/stores.html', {'stores': stores})

def product(request, product_id):
    try:
        product = Product.objects.filter(id=product_id).get()
    except Product.DoesNotExist:
        raise Http404("Товар не найден")
    return render(request, 'sanek/product.html', {'product': product})

def store(request, store_id):
    try:
        store = Store.objects.filter(id=store_id).get()
        products = Product.objects.filter(store=store)
    except Store.DoesNotExist:
        raise Http404("Магазин не найден")
    return render(request, 'sanek/store.html', {
        'store': store,
        'products': products,
    })