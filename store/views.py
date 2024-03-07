from django.shortcuts import render
from django.http import JsonResponse , HttpResponseNotAllowed
import json

from .models import *

# Create your views here.
def store(request):
    products= Product.objects.all()
    context={'products': products}
    return render(request, 'store.html', context)
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else :
        items=[]
        order={'get_cart_total': 0, 'get_item_total':0}

    context={'items':items, 'order': order }
    return render(request,'cart.html', context)
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
    else :
        items=[]
        order={'get_cart_total': 0, 'get_item_total':0}

    context={'items':items, 'order': order }
    
    return render(request,'checkout.html', context)
def updateItem(request):
   
        data=json.loads(request.body)
        productId=data['productId']
        action = data['action']
        print('action :', action )
        print('productId:', productId)
        customer=request.user.customer
        product= Product.objects.get(id=productId)
        order, created= Order.objects.get_or_create(customer= customer, complete= False )
        orderItem, created=OrderItem.objects.get_or_create(order=order, product=product )
        if action == 'add':
            orderItem.quantity=orderItem.quantity+1
        elif action=='remove':
            orderItem.quantity= orderItem.quantity-1
        orderItem.save()
        if orderItem.quantity<=0:
            orderItem.delete()



        return JsonResponse('item was added', safe=False )# safe= False in the case of just a string ,
        #if you pass a non-dictionary, non-list, or non-queryset object and set safe=True, Django will raise a TypeError
   




