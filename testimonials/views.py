from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TestimonialsForm
from .models import Testimonials


def testimonial(request):
    if request.method == 'POST':
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Thank you, we have received your testimonial!')
            return redirect('all/')
    else:
        form = TestimonialsForm()
    return render(request, 'testimonials/testimonial.html', {'form': form})


def testimonial_all(request):
    testimonials = Testimonials.objects.all().order_by('-id')[:5]

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/all.html', context)
