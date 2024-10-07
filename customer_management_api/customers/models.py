from django.db import models
import random
import string
def generate_unique_id(model_class, field_name):
    while True:
        unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        if not model_class.objects.filter(**{field_name: unique_id}).exists():
            return unique_id


class Customer(models.Model):
    customer_id = models.CharField(max_length=8, unique=True, editable=False, primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.customer_id:
            self.customer_id = generate_unique_id(Customer, 'customer_id')
        super().save(*args, **kwargs)


class Order(models.Model):
    order_id = models.CharField(max_length=8, unique=True, editable=False, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    item = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item + "-" + str(self.amount)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_unique_id(Order, 'order_id')
        super().save(*args, **kwargs)


