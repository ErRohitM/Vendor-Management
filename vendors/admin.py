from django.contrib import admin
from . models import Vendor_Details,PO_Details,Historical_Performance

admin.site.register(PO_Details)
admin.site.register(Vendor_Details)
admin.site.register(Historical_Performance)