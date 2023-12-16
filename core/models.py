from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=25)
    mobile_no = models.IntegerField()
    pin_code = models.IntegerField()  


    def __str__(self):
        return self.customer_name


class Product(models.Model):
    product_name = models.CharField(max_length=25)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="customer_info")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product_info")
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
