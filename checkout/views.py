from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key' : 'pk_test_51J7bkAAkIYnOVpTZhjFjCpRButaRd5VKNS4Yu7k0thODm2azoigW1h6RchyIUd98UgPV0Nh1OemAM2b2HpQqdRsv00QowWGNKX','client_secret' :'test_key'
    }

    return render(request, template, context)