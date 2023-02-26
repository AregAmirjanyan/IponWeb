import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from polls.models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBug, Purchase
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class ItemView(View):
    
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
    
        items = Item.objects.all()
        data = []
        for item in items:
            
            data.append({"name": item.name, 'price' : str(item.price), 'item_category': item.category.id, 'quantity' : item.quantity})
        return ItemView.data_status(data)
    
    
    def post(self, request):
        data = json.loads(request.body)
        item = Item.objects.create(
            name = data['name'], price = data['price'], quantity = data['quantity']
            
            )
        item.save()
        return self.ok_status()
    
    
    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemView.get_single(request, id)
        if request.method == "DELETE":
            return ItemView.delete(request, id)
        if request.method == "PATCH":
            return ItemView.edit(request, id)
    
    
    @staticmethod
    def get_single(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return ItemView.data_status({"name": item.name, 'price' : str(item.price), 'item_category': item.category.id, 'quantity' : item.quantity})
    
    
    
    @staticmethod
    def delete(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        item.delete()
        return ItemView.ok_status()
    
    
    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            item.name = data['name']
        if "price" in data:
            item.price = data['item']
        if "quantity" in data:
            item.quantity = data['quantity']
        
        item.save()
        return ItemView.ok_status()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    