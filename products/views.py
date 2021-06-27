from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def portfolio_years(request):
    """ A view to show all years of works """

    return render(request, 'products/portfolio.html')

def media(request):
    """ A view to show all media from previously selected year """

    return render(request, 'products/media.html')


def all_products(request):
    """ A view to show all works, including sorting and search queries """

    products = Product.objects.all()

    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            cat = products.filter(category__name__in=categories)
            if 'date' in request.GET:
                dates = request.GET['date'].split(',')
                date = cat.filter(date__in=dates)
            


    context = {
        'cat': cat,
        'date' : date
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show the individual work """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)