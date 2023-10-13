from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactInquiriesForm


def contact(request):
    """
    Display the contact form.
    """
    if request.method == 'POST':
        form = ContactInquiriesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'We received your query! We will contact you within 48 hours.')
            return redirect('contact')
    else:
        form = ContactInquiriesForm()
    return render(request, 'contact_form/contact_form.html', {'form': form})
