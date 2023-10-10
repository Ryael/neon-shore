from django.contrib import admin
from .models import ContactInquiries

# Register your models here.

class ContactInquiriesAdmin(admin.ModelAdmin):
    baseModel = ContactInquiries
    list_display = (
      'name',
      'email',
      'subject',
      'message',
      )

admin.site.register(ContactInquiries)
