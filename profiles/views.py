from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's overall profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)

def profile_details(request):
    """ Display the user's profile details. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/details.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

def profile_orders(request):
    """ Display the user's orders. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/orders.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)

def profile_account(request):
    """ Display the user's account information. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/account.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
