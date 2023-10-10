from django import forms
from django.core.validators import EmailValidator
from .models import ContactInquiries


class ContactInquiriesForm(forms.ModelForm):

    class Meta:
        model = ContactInquiries
        fields = '__all__'

    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

