from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Testimonials(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_received = models.DateTimeField(auto_now_add=True)
    review = models.TextField(null=False, blank=False, max_length=1500)

    class Meta:
        verbose_name_plural = "Testimonials"
