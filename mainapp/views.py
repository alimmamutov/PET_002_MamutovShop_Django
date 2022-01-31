from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from mainapp.models import ProductCategory, Product


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def shop(request, id_category=None):
    if id_category:
        product_list = Product.objects.filter(category_id=id_category)
    else:
        product_list = Product.objects.all()

    context = {
        'title': 'Магазин',
        'category_list': ProductCategory.objects.all(),
        'product_list': product_list
    }
    return render(request, 'mainapp/shop.html', context)


def detail(request, pk):
    context = {
        'title': 'Карточка продукта'
    }
    return render(request, 'mainapp/detail.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)


