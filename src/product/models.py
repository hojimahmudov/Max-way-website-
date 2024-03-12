from django.db import models
from user.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True, editable=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, db_index=True)
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    title_image = models.ImageField(upload_to="images/", null=True, blank=True)
    discription = models.TextField(null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class UserBasket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Basket(models.Model):
    count = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user_basket = models.OneToOneField(UserBasket, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s - %s" % (self.id, self.product)



