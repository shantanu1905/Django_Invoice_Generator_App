from django.urls import path
from django.contrib import admin
from invoice_app.views import *
from .views import *

urlpatterns = [
   path('', home, name="home"),
   path('list/', Invoice_list.as_view(), name="Invoice_list"),
   path('list/add/', Add_invoice, name="Add_invoice"),
   path('delete/<int:Invoice_id>/' ,delete, name='delete'),
   path('details/<int:Invoice_id>/', details, name='details' ),
   





  
]