from rest_framework import serializers
from . models import Vendor_Details, PO_Details, Historical_Performance
     
class Vendors_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_Details
        fields = ['vendor_name', 'contact_details','vendor_address']
        #fields = '__all__'
           

class Purchase_Order_Serializer(serializers.ModelSerializer):
    #vendor_id = serializers.PrimaryKeyRelatedField(queryset=Vendor_Details.objects.all())
    class Meta:
        model = PO_Details
        fields = '__all__'
        

class Vendor_Performance_Serializer(serializers.ModelSerializer):
    vendor_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Historical_Performance
        fields = '__all__'
        

class Update_Acknowledgment(serializers.ModelSerializer):
    class Meta:
        model = PO_Details
        fields = ['acknowledgment_date']