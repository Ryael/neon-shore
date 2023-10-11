from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TestimonialsForm


def testimonial(request):
    if request.method == 'POST':
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            form.user=request.user_id
            form.save()
            messages.success(request, 'Thank you, we received your testimonial!')
            return redirect('testimonials')
    else:
        form = TestimonialsForm()
    return render(request, 'testimonials/testimonial.html', {'form': form})
