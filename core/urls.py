from django.urls import path
from .views import *



urlpatterns = [
    path('', CreateOrderView, name="createorder"),
    path('get_unit_price/', get_unit_price, name='get_unit_price'),
    path('orderlist/', orderlist, name="orderlist"),
    path('orderupdate/<int:id>/', orderupdate, name="orderupdate"),
    path('orderdelete/<int:id>/', orderdelete, name="orderdelete"),
]
   