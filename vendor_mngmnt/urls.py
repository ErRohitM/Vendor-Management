
from django.contrib import admin
from django.urls import path, include
from vendors import views

urlpatterns = [
    path('api/', include('vendors.urls')),
    path('admin/', admin.site.urls),
]
