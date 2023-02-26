import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from polls.models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBug, Purchase


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class PurchaseView(View):
    
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
        purchases = Purchase.objects.all()
        data = []
        for purchase in purchases:
            data.append({'customer_id' : purchase.customer.id, 'total_price' : str(purchase.total_price)})
        return PurchaseView.data_status(data)
    
    
    def post(self, request):
        data = json.loads(request.body)
        customer= Customer.objects.get(id = data['customer'])
        item = Item.objects.get(id = data['item'])
        
        
        purchase = Purchase.objects.create(
            total_price=data['total_price'],
            customer = customer,
            item = item
            
            )
        purchase.save()
        return self.ok_status()
    
    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return PurchaseView.get_single(request, id)
        if request.method == "DELETE":
            return PurchaseView.delete(request, id)
        if request.method == "PATCH":
            return PurchaseView.edit(request, id)
    
    
    @staticmethod
    def get_single(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return PurchaseView.data_status({'customer_id' : purchase.customer.id, 'total_price' : str(purchase.total_price)})
    
    
    
    @staticmethod
    def delete(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        purchase.delete()
        return PurchaseView.ok_status()
    
    
    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        if "customer_id" in data:
            purchase.customer_id = data['customer_id']
        if "total_price" in data:
            purchase.total_price = data['total_price']
            
        purchase.save()
        return PurchaseView.ok_status()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    