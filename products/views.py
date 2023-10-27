from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from user.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'products':Product.objects.all(),
        'categories':ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product,quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])