from django.contrib import admin
from .models import ContactInquiries

# Register your models here.

class ContactInquiriesAdmin(admin.ModelAdmin):
    list_display = (
      'name',
      'email',
      'subject',
      'message',
      'date_received',
      )
    ordering = ('-date_received',)

admin.site.register(ContactInquiries)
