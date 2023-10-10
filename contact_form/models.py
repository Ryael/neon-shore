from django.db import models

# Create your models here.

class ContactInquiries(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    email = models.EmailField(null=False, blank=False, max_length=50)
    subject = models.CharField(max_length=200)
    message = models.TextField(null=False, blank=False, max_length=3000)
    date_received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" message from {self.email}"

    class Meta:
        verbose_name_plural = "Contact Inquiries"
