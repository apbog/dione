from django.shortcuts import render


def home_page(request):
    return render(request, 'landing/home.html')


def landing_page(request):
    return render(request, 'landing/start.html')


def product_page(request):
    return render(request, 'landing/product.html')

# TODO: Add views to Task objects
