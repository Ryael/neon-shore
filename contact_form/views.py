from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'We received your query! We will contact you within 48 hours.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact_form/contact_form.html', {'form': form})
