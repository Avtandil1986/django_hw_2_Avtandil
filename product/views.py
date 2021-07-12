from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product


def main_page_view(request):
    products = Product.objects.all()
    print(products)
    for i in products:
        print('id:', i.id)
        print('title:', i.title)
        print('price:', i.price)
        print()
    data = {
        'title': 'Главная страница',
        'product_list': products
    }
    return render(request, 'index.html', context=data)


def product_item_view(request, product_id):
    product = Product.objects.get(id=product_id)
    data = {
        'product': product,
        'title': product.title,
    }
    return render(request, 'item.html', context=data)