from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Testimonials(models.Model):
    """ Model to store all testimonials. """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_received = models.DateTimeField(auto_now_add=True)
    testimonial = models.TextField(null=False, blank=False, max_length=100)

    def __str__(self):
        return f"Testimonial from {self.user}."

    class Meta:
        verbose_name_plural = "Testimonials"
