from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    """ Model for the category of products. """

    class Meta:
        """"
        Changes the name of the category in the admin panel.
        """
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    singular_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Passes the friendly name to the template/admin panel.
        """
        return self.friendly_name

    def get_singular_name(self):
        """
        Passes the singular name to the template/admin panel
        """
        return self.singular_name


class Product(models.Model):
    """ Model for all products. """

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class WishlistItem (models.Model):
    """ Model for wishlist items. """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
