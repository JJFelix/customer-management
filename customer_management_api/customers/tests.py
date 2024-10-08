from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer, Order

class CustomerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name="John Smith", phone="+254741022295")

    def test_get_customers(self):
        response = self.client.get(reverse('get_customers'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customer(self):
        response = self.client.get(reverse('get_customer', args=[self.customer.customer_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_customer(self):
        data = {"name": "John Smith", "phone": "+254741022294"}
        response = self.client.post(reverse('add_customer'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_customer(self):
        response = self.client.delete(reverse('delete_customer', args=[self.customer.customer_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class OrderTests(TestCase):
    def setUp(self):
        self.client2 = APIClient()
        # customer instance
        self.customer = Customer.objects.create(name="John Smith", phone="+254742378490")
        self.order = Order.objects.create(customer=self.customer, item="Cement", amount=20)

    def test_get_orders(self):
            response = self.client2.get(reverse('get_orders'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_order(self):
        data = {"customer": self.customer.customer_id, "item": "Sugar", "amount": 10}
        response = self.client2.post(reverse('add_order'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_order(self):
        response = self.client2.delete(reverse('delete_order', args=[self.order.order_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
