from model_mommy import mommy

from django.urls import reverse

from core.tests import BaseAPITestCase
from .models import Order


class OrdersAPITestCase(BaseAPITestCase):

    list_url = reverse('order-list')

    def setUp(self):
        super(AccountsAPITestCase, self).setUp()
        self.roger_order = mommy.make(
            'orders.Order',
            name='Roger Order 1',
            created_by=self.roger_user,
        )
        mommy.make('orders.Order', name='Roger Order 2', created_by=self.roger_user)
        mommy.make('orders.Order', name='Sally Order 1', created_by=self.sally_user)

        self.roger_detail_url = reverse('order-detail', kwargs={
            'pk': self.roger_order.id,
        })

    def test_can_fetch_orders(self):
        response = self.roger_client.get(self.list_url)
        self.assertEqual(len(response.json()), Item.objects.count())

    def test_can_create_order(self):
        payload = {'name': 'Roger Item 3', 'price': '3.25'}
        response = self.roger_client.post(self.list_url, payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('createdBy'), self.roger_user.id)

