from django.shortcuts import render, get_object_or_404
from .models import Product

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

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show the individual work """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)