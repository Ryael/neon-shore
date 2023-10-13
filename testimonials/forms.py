from django import forms
from django.core.validators import EmailValidator
from .models import Testimonials


class TestimonialsForm(forms.ModelForm):
    """ Form to input testimonials. """

    class Meta:
        model = Testimonials
        fields = '__all__'
        exclude = ('user',)

    testimonial = forms.CharField(widget=forms.Textarea, max_length=100)
