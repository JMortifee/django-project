from django.shortcuts import render,redirect
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    q = product.quantity
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        if bag[item_id] == q :
            print('no more available')
            print(request.session['bag'])
            # below statement need to return a message saying no more available
            return redirect(redirect_url)
        else:
            bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)