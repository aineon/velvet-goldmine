from django.shortcuts import (render, reverse, get_object_or_404,
                              HttpResponseRedirect)
from django.contrib import messages
from django.utils.html import format_html
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from products.models import Product


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed.'
                           'Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """Get all past orders of the user"""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def favourite_product(request, product_id):
    """Add a product to the users favourites"""
    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        if product.favourites.filter(id=request.user.id).exists():
            product.favourites.remove(request.user)
            messages.success(request, f'{product.name} \
                                removed from your favourites')
        else:
            product.favourites.add(request.user)
            messages.success(request, f'{product.name} \
                                added to your favourites')
    else:
        message1 = format_html('Sorry! You need to be logged in to save a product. \
                              <a href="{}">sign in</a>', reverse(
                              'account_login'))
        message2 = format_html(' or <a href="{}">sign up</a>', reverse(
                              'account_signup'))
        messages.error(request, message1 + message2)

    # refresh current page
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def fav_products_list(request):
    """Get Users favourite products"""
    fav_products = Product.objects.filter(favourites=request.user)
    print(fav_products)
    template = 'profile.html'
    context = {
         'fav_products': fav_products,
    }

    return render(request, template, context)
