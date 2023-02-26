import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from polls.models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBug, Purchase
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class StoreOwnerView(View):
    
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
    
        owners = StoreOwner.objects.all()
        data = []
        for owner in owners:
            
            data.append({"user_id": owner.user.id, 'avatar_dir' : owner.avatar.url})
        return StoreOwnerView.data_status(data)
    
    
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(id = data['user_id'])
        avatar = data['avatar']
        owner = StoreOwner.objects.create(
            user = user, avatar = avatar
            
            )
        owner.save()
        return self.ok_status()
    
    
    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwnerView.get_single(request, id)
        if request.method == "DELETE":
            return StoreOwnerView.delete(request, id)
        if request.method == "PATCH":
            return StoreOwnerView.edit(request, id)
    
    
    @staticmethod
    def get_single(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreOwnerView.data_status({"id": owner.id, "owner_id": owner.user.id})
    
    
    
    @staticmethod
    def delete(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        owner.delete()
        return StoreOwnerView.ok_status()
    
    
    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            owner.name = data['name']
            
        if "user_id" in data:
            owner.id = data['user_id']
        owner.save()
        return StoreOwnerView.ok_status()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    