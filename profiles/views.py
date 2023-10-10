from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order
from products.models import WishlistItem
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def profile(request):
    """ Display the user's overall profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def profile_details(request):
    """ Display the user's profile details. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/details.html'
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)


@login_required
def profile_orders(request):
    """ Display the user's orders. """
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/orders.html'
    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
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


@login_required
def profile_account(request):
    """ Display the user's account information. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/account.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def profile_admin(request):
    """ Display product management to admins. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/admin.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def profile_wishlist(request):
    """ Display the user's wishlist. """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = WishlistItem.objects.filter(user_id=request.user.id)

    template = 'profiles/wishlist.html'
    context = {
        'profile': profile,
        'wishlist': wishlist,
    }

    return render(request, template, context)

