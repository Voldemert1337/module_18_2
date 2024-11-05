from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'second_task/class_template.html')


def functionality(request):
    return render(request, 'second_task/func_template.html')


def home(request):
    return render(request, 'third_task/home.html')


def about(request):
    return render(request, 'third_task/about.html')


def products(request):
    return render(request, 'third_task/products.html')