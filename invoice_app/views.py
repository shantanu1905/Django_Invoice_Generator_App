# Create your views here.
import re
from django.shortcuts import render , redirect
from django.contrib import messages
from django.views.generic import (ListView , CreateView , DetailView , FormView)
from django.views.generic.detail import SingleObjectMixin
from .models import *

def home(request):
    return render(request , "base.html")


class Invoice_list(ListView):
    model = Invoice
    template_name="invoice_list.html"


def Add_invoice(request):
    if request.method == "POST":
        customer= request.POST['customer']
        email= request.POST['email']
        msg= request.POST['msg']
        address= request.POST['bill_address']

        #listitem data
        i1= request.POST['i1']
        i2= request.POST['i2']
        i3= request.POST['i3']
        ic1= request.POST['ic1']
        ic2= request.POST['ic2']
        ic3= request.POST['ic3']
        total= request.POST['total']
   


        data=Invoice(customer=customer ,  customer_email=email, billing_address= address, message=msg , i1=i1, i2=i2, i3=i3, ic1=ic1, ic2=ic2, ic3=ic3 , total=total)
        data.save()
      

        messages.success(request, 'your Invoice is created , click edit to add more details')
        

    return render(request , "create_invoice.html")
   

def delete(request , Invoice_id):
    item= Invoice.objects.get(pk=Invoice_id)
    item.delete()
    messages.success(request, 'your Task has been deleted successfullly')
    return render(request , "base.html")



def details(request , Invoice_id):
    context ={}
    # add the dictionary during initialization
    context["Invoice"] = Invoice.objects.get(pk=Invoice_id)

    return render(request , "invoice_details.html" , context)

