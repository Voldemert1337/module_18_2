from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'fourth_task/home.html')


def about(request):
    return render(request, 'fourth_task/about.html')


def products(request):
    return render(request, 'fourth_task/products.html')