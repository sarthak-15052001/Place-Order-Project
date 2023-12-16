from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import *
from .forms import *
import json
from django.contrib import messages

# Create your views here.

def CreateOrderView(request):
    template_name = 'core/add-order.html'

    if request.method == 'POST':
        form = OrderForm(request.POST)  
        if form.is_valid():
            customer = form.cleaned_data['customer']
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            total_price = form.cleaned_data['total_price']

            reg = Order(customer=customer, product=product, quantity=quantity, total_price=total_price)
            reg.save()
            messages.success(request, "Order Placed Successfully!!")
            return redirect("createorder")
    else:
        form = OrderForm()
        stud = Order.objects.all()
        return render(request, template_name, {"form": form, "stu":stud})



def get_unit_price(request):
    product_id = request.POST.get("id")
    product = Product.objects.values('unit_price').get(id=product_id)
    response = {"product_unit_price":str(product["unit_price"])}
    return HttpResponse(json.dumps(response), content_type="application/json")


def orderlist(request):
    form = Order.objects.all()
    return render(request, "core/order-list.html", {"form":form})



def orderupdate(request, id):
    if request.method == "POST":
        id = Order.objects.get(pk=id)
        form = OrderForm(request.POST, instance=id)
        if form.is_valid():
            form.save()
            messages.success(request, "Order Updated Successfully!!")
        return redirect('orderupdate', id=id.pk)
    else:
        id = Order.objects.get(pk=id)
        form = OrderForm(instance=id)
    return render(request, 'core/update-order.html', {"form":form})

def orderdelete(request, id):
    if request.method == "POST":
        pi = Order.objects.get(pk=id)
        pi.delete()
        return redirect('orderlist')
    else:
        return render(request, 'core/delete-order.html', context={'message': 'Invalid request method'})
