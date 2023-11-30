from django.urls import path, include
from .import views

urlpatterns = [
    path('vendors/', views.VendorsListorCreateView.as_view(), name='listorcreate_vendors'),
    path('vendors/<int:pk>', views.VendorDetailsView.as_view(), name='vendor_detailed'),
    path('purchase_orders/', views.PurchasesListorCreateView.as_view(), name='listorcreate_po'),
    path('purchase_orders/<int:pk>', views.PO_DetailsView.as_view(), name='po_detailed'),
    path('vendors/<int:pk>/performance/', views.Vendor_PerformanceListView.as_view(), name='vendor_performance'),
    path('purchase_orders/<int:pk>/acknowledge', views.Acknowledgment_by_Vendor.as_view(), name='vendor_ack'),
]
