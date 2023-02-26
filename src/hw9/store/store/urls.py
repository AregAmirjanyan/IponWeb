"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static 
from api.storecategory import StoreCategoryView
from api.item_category import ItemCategoryView
from api.customer import CustomerView
from api.store_owner import StoreOwnerView
from api.store import StoreView
from api.item import ItemView
from api.my_bag import MyBagView
from api.purchase import PurchaseView







urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('storecategory/', StoreCategoryView.as_view()),
    path('itemcategory/', ItemCategoryView.as_view()),
    path('customer/', CustomerView.as_view()),
    path('storeowner/', StoreOwnerView.as_view()),
    path('store/', StoreView.as_view()),
    path('item/', ItemView.as_view()),
    path('mybag/', MyBagView.as_view()),
    path('purchase/', PurchaseView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)