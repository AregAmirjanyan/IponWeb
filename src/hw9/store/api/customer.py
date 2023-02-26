import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from polls.models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBug, Purchase
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class CustomerView(View):
    
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
    
        customers = Customer.objects.all()
        data = []
        for customer in customers:
            
            data.append({"user_id": customer.user.id, 'avatar_dir' : customer.avatar.url})
        return CustomerView.data_status(data)
    
    
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(id = data['user_id'])
        avatar = data['avatar']
        customer = Customer.objects.create(
            user = user, avatar = avatar
            
            )
        customer.save()
        return self.ok_status()
    
    
    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return CustomerView.get_single(request, id)
        if request.method == "DELETE":
            return CustomerView.delete(request, id)
        if request.method == "PATCH":
            return CustomerView.edit(request, id)
    
    
    @staticmethod
    def get_single(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return CustomerView.data_status({"id": customer.id, "username": customer.user})
    
    
    
    @staticmethod
    def delete(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        customer.delete()
        return CustomerView.ok_status()
    
    
    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            customer.name = data['name']
        customer.save()
        return CustomerView.ok_status()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    