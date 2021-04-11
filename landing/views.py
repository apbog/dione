from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home_page(request):
    return render(request, 'landing/home.html')


@login_required(login_url='/login/')
def landing_page(request):
    return render(request, 'landing/start.html')


def product_page(request):
    return render(request, 'landing/product.html')

# TODO: Add views to Task objects
