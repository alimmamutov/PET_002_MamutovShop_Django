from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def product(request):
    return render(request, 'mainapp/product.html')


def contact(request):
    return render(request, 'mainapp/contact.html')