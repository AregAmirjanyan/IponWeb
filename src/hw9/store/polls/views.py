import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from rest_framework.response import Response 
from .models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBug, Purchase


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




        
    
    
    