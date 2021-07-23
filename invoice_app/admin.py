from django.contrib import admin

# Register your models here.
from .models import Invoice, LineItem

admin.site.register(Invoice)
admin.site.register(LineItem)