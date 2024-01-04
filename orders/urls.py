from django.conf import settings
from django.urls import include, path

from orders.views import OrderCreateView, SuccessView,CansellView, OrdersView, OrderListView

app_name = 'orders'
urlpatterns = [
    path('order/', OrderCreateView.as_view(), name='order'),
    path('success/',SuccessView.as_view(), name='success'),
    path('cancel/',CansellView.as_view(), name='cancel'),
    path('',OrdersView.as_view(), name='orders_list'),
    path('order/<int:pk>/',OrderListView.as_view(), name='order'),
]
