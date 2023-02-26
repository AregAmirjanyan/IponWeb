import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from polls.models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBug, Purchase
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class MyBagView(View):
    
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            status=200,
            content_type="application/json",
        )
    
    
    @staticmethod
    def ok_status():
        return HttpResponse(
            json.dumps({"status": "ok"}), status=200, content_type="application/json"
        )
    
    
    def get(self, request): 
    
        bags = MyBug.objects.all()
        data = []
        for bag in bags:
            
            data.append({"customer_id": bag.customer.id, 'total_price' : str(bag.total_price) })
        return MyBagView.data_status(data)
    
    
    def post(self, request):
        data = json.loads(request.body)
        customer= Customer.objects.get(id = data['customer'])
        item = Item.objects.get(id = data['item'])
        bag = MyBug.objects.create(
            total_price = data['total_price'], customer = customer, item = item
            
            )
        bag.save()
        return self.ok_status()
    
    
    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return MyBagView.get_single(request, id)
        if request.method == "DELETE":
            return MyBagView.delete(request, id)
        if request.method == "PATCH":
            return MyBagView.edit(request, id)
    
    
    @staticmethod
    def get_single(request, id):
        try:
            bag = MyBug.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return MyBagView.data_status({"customer_id": bag.customer.id, 'total_price' : str(bag.total_price)})
    
    
    
    @staticmethod
    def delete(request, id):
        try:
            bag = MyBug.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        bag.delete()
        return MyBagView.ok_status()
    
    
    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            bag = MyBug.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "customer_id" in data:
            bag.customer_id = data['customer_id']
        if "total_price" in data:
            bag.total_price = data['total_price']
        
        bag.save()
        return MyBagView.ok_status()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    