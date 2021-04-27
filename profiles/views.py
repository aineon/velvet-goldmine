from django.shortcuts import (render, reverse, redirect,
                              get_object_or_404,
                              HttpResponseRedirect)
from django.conf import settings
from django.contrib import messages
from django.utils.html import format_html
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template

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
            messages.success(request, 'Delivery info updated successfully')
        else:
            messages.error(request, 'Update failed.'
                           'Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    # Arrange orders by most recent
    orders = profile.orders.all().order_by('-date')
    # Add users favourite products to their profile
    products = Product.objects.all()
    fav_products = products.filter(favourites=request.user)
    is_favourite = True

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'fav_products': fav_products,
        'is_favourite': is_favourite,
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
            item = product.name
            message = format_html(item + ' added to your favourites. \
                 View <a href="{}">Your Favourites</a>', reverse('profile'))
            messages.success(request, message)
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
    products = Product.objects.all()
    fav_products = products.filter(favourites=request.user)

    template = 'profile.html'
    context = {
         'fav_products': fav_products,
    }

    return render(request, template, context)


def deactivate_account(request):
    """Deactivate users account"""
    user = request.user
    user.is_active = False
    # Send email confirming account deactivation
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [user.email]
    subject = 'Account Deactivation Successful'
    body = render_to_string(
        'profiles/confirmation_emails/deactivate_account_confirm_body.txt')
    deactivation_confirmation_email = EmailMultiAlternatives(
                                        subject=subject,
                                        body=body,
                                        from_email=from_email,
                                        to=to_email)
    html_template = get_template(
        'profiles/confirmation_emails/deactivate_account_confirm_body.html'
        ).render()
    deactivation_confirmation_email.attach_alternative(html_template,
                                                       'text/html')
    deactivation_confirmation_email.send()
    user.save()
    messages.success(request, 'Your account has been deactivated')
    return redirect('products')
