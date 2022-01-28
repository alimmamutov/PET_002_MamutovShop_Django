from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def shop(request):
    context = {
        'title': 'Магазин'
    }
    return render(request, 'mainapp/shop.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)