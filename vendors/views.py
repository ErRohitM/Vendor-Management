from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin,CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Vendor_Details, PO_Details, Historical_Performance
from . serializers import Vendors_Serializer, Purchase_Order_Serializer,Vendor_Performance_Serializer,Update_Acknowledgment





#class Create_Vendor(APIView):
 #   def post(request):
  #      serializer = Create_New_Vendor_Serializer(data = request.data)
   #     serializer.is_valid()
    #    serializer.save()
     #   return Response(serializer.data)
    
class VendorsListorCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Vendor_Details.objects.all()
    serializer_class = Vendors_Serializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class VendorDetailsView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Vendor_Details.objects.all()
    serializer_class = Vendors_Serializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
class PurchasesListorCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = PO_Details.objects.all()
    serializer_class = Purchase_Order_Serializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class PO_DetailsView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = PO_Details.objects.all()
    serializer_class = Purchase_Order_Serializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
#create Vendor_Performance endpoint 
class Vendor_PerformanceListView(GenericAPIView, RetrieveModelMixin):
    queryset = Historical_Performance.objects.all()
    serializer_class = Vendor_Performance_Serializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class Acknowledgment_by_Vendor(GenericAPIView, RetrieveModelMixin, UpdateModelMixin):
    queryset = PO_Details.objects.all()
    serializer_class = Update_Acknowledgment
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    