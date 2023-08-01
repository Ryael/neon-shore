from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """ Display the user's overall profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)

def profile_details(request):
    """ Display the user's details. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/details.html'
    context = {
        'profile': profile,
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
