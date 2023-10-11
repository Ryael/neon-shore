from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from .models import Testimonials


class TestimonialsForm(forms.ModelForm):

    class Meta:
        model = Testimonials
        fields = '__all__'
        exclude = ('user',)

    review = forms.CharField(widget=forms.Textarea)


