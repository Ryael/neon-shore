from django.contrib import admin
from .models import Testimonials

# Register your models here.

class TestimonialsAdmin(admin.ModelAdmin):
    baseModel = Testimonials
    list_display = (
      'user',
      'review'
      )

admin.site.register(Testimonials)

