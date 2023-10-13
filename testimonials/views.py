from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TestimonialsForm
from .models import Testimonials


@login_required
def testimonial(request):
    """ Display the add testimonial page. """
    if request.method == 'POST':
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request,
                             'Thank you, we have received your testimonial!')
            return redirect('all/')
    else:
        form = TestimonialsForm()
    return render(request, 'testimonials/testimonial.html', {'form': form})


def testimonial_all(request):
    """ Display all testimonials. """
    testimonials = Testimonials.objects.all().order_by('-id')[:5]

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/all.html', context)
