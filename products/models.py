import stripe
from django.db import models

from user.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "категорию продукта"
        verbose_name_plural = "Категория продукта"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    stripe_product_basket_id = models.CharField(max_length=128, null=True, blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "Продукт"

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.description}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.stripe_product_basket_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_basket_id = stripe_product_price['id']
            super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'],
            unit_amount=round(self.price * 100),
            currency='rub'
        )
        return stripe_product_price


# Расширил objects, добавив свои методы
class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def stripe_products(self):
        line_items = []
        for basket in self:
            item = {
                'price': basket.products.stripe_product_basket_id,
                'quantity': basket.quantity
            }
            line_items.append(item)
        return line_items


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = "корзину"
        verbose_name_plural = "Корзина"

    def __str__(self):
        return f"Корзина для {self.user.username} | Продукт: {self.products.name}"

    # Метод нахождения суммы товаров
    def sum(self):
        return self.products.price * self.quantity

    def de_json(self):
        basket_item  ={
            'product_name': self.products.name,
            'quantity': self.quantity,
            'price': float(self.products.price),
            'sum': float(self.sum()),
        }
        return basket_item