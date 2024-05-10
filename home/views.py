from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def index(request):
    category = Category.objects.all()

    context = {
        'category':category
    }
    return render(request, 'index.html', context)

def product(request):
    product = Product.objects.all()

    context = {
        'product':product
    }
    return render(request, 'product.html', context)

# def product_detail(request):
#     return render(request, 'product.html')

def signup(request):
    return render(request, 'signin.html')

def signin(request):
    return render(request, 'signup.html')