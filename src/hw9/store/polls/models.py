from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class StoreCategory(models.Model):
    name = models.CharField(max_length = 255, db_index = True)
    picture = models.ImageField(upload_to = 'store/', blank = True, null =True)
    date = models.DateTimeField(default = timezone.now)
    
    def __repr__(self):
        return self.name
    
    

class ItemCategory(models.Model):
    name = models.CharField(max_length = 255, db_index = True)
    picture = models.ImageField(upload_to = 'item/', blank = True, null =True)
    date = models.DateTimeField(default = timezone.now)
    
    def __repr__(self):
        return self.name
    
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to ="customers/", blank = True, null =True)
    registered_at = models.DateTimeField(default = timezone.now)
    

class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to ="storeowner/", blank = True, null =True)
    registered_at = models.DateTimeField(default = timezone.now)
    
    
class Store(models.Model):
    name = models.CharField(max_length = 255, db_index = True)
    owner = models.ForeignKey(StoreOwner, on_delete = models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete = models.CASCADE)
    
    def __repr__(self):
        return self.name
    

class Item(models.Model):
    name = models.CharField(max_length = 255, db_index = True)
    picture = models.ImageField(upload_to = 'item/', blank = True, null =True)
    category = models.ForeignKey(ItemCategory, on_delete = models.CASCADE)
    price = models.DecimalField(null = True, max_digits = 10, decimal_places = 2)
    quantity = models.IntegerField(default=1)
    info = models.CharField(max_length = 255, db_index = True)
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    
    def __repr__(self):
        return self.name
    
    
class MyBug(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.IntegerField(default=1)
   
   
class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(default = timezone.now)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    total_price = models.IntegerField(default=1)
    
    
    
    
    
    
    
    
    
    
    