from django.db import models

# Create your models here.
class Invoice(models.Model):
    customer = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    
    message = models.TextField(default= "None")

    i1 = models.TextField(default= "None")
    ic1 = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    i2 = models.TextField(default= "None")
    ic2 = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    i3 = models.TextField(default= "None")
    ic3 = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)









    
    total = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
   
    def __str__(self):
        return str(self.customer)

class LineItem(models.Model):
    customer = models.ForeignKey(Invoice, on_delete=models.CASCADE)
 

 




    def __str__(self):
        return str(self.customer)