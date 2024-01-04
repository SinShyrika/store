import os
import django

if 'env setting':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
    django.setup()
from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from products.models import Product, ProductCategory


class HomeViewTestCase(TestCase):

    def test_view(self):
        path = reverse('home')
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Store')


class ProductsListViewTestCase(TestCase):
    fixtures = ['category.json', 'products.json']

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_test(response)
        self.assertEqual(list(response.context_data['object_list']),
                         list(self.products[:3]))  # QuerySet1 != QuerySet2 but list1 == list2

    def test_list_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self._common_test(response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=category.id))

        )

        print(response.context_data['object_list'])
        print(self.products.filter(category_id=category.id))

    def _common_test(self,response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')

