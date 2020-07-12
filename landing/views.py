from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'landing/home.html')


def landing_page(request):
    return render(request, 'landing/start.html')
