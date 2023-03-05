from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Category, Product


def index(request):
    return HttpResponse('Reservas')


def product_list(request):
    products = Product.objects.filter(status='a').order_by('id')
    return render(request, 'bookings/product_list.html', {'products': products})


def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.category = Category.objects.get(id=1)
            product.status = 'a'
            product.save()
            return redirect('bookings:product_list')
    else:
        form = ProductForm()
    return render(request, 'bookings/product_edit.html', {'form': form})
