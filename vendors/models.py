from django.db import models
from django.db.models import Count, F, ExpressionWrapper, FloatField
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date, timedelta
from django.urls import reverse

class Vendor_Details(models.Model):
    vendor_name = models.CharField(max_length=255, verbose_name='username')
    contact_details = models.TextField()
    vendor_address = models.TextField()
    vendor_code = models.SlugField(max_length=300, null=True, blank=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(blank=True, default=0.0)
    average_response_time = models.DurationField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)
    
    class Meta:
        ordering = ['-id']
        def __str__(self):
            return f'{self.vendor_code}'
    
    #sluggify vendor_code
    def save(self, *args, **kwargs):
        self.vendor_code = slugify(self.vendor_name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.vendor_name
        
        
    def get_absolute_url(self):
        return reverse('vendors:detail', kwargs={'pk': self.id})     

    

class PO_Details(models.Model):
    Po_status = {
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Delivered', 'Delivered')
    }
    po_number = models.CharField(max_length=150, unique=True)
    vendor = models.ForeignKey(Vendor_Details, on_delete=models.CASCADE, related_name='vendor_set')
    order_date = models.DateField(default=date.today)
    delivery_date = models.DateField(auto_now_add=False)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.TextField(max_length=255, choices=Po_status)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()
    
class Historical_Performance(models.Model):
    vendor = models.ForeignKey(Vendor_Details, on_delete=models.CASCADE, related_name='vendor_performance')
    date = models.DateField(default=date.today)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(blank=True, default=0.0)
    average_response_time = models.DurationField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Historical Performance"
        
        
    def __str__(self):
        return self.vendor.vendor_name
    
    
    @receiver(post_save, sender=PO_Details)
    def calculate_historical_performance_on_time_delivery_rate(sender, instance, created, **kwargs):
        if created and instance.status == 'Delivered':
            vendor = instance.vendor
            
            historical_performance, created = Historical_Performance.objects.get_or_create(
                vendor=vendor,
                date=date.today()
            )
            
            vendor_model = Vendor_Details.objects.filter(vendor_name = vendor.vendor_name)
            
            completed_pos = vendor.vendor_set.filter(status='Delivered').count()

            # Avoid division by zero
            if completed_pos > 0:
                on_time_delivery_count = vendor.vendor_set.filter(
                    status='Delivered',
                    delivery_date__lte=F('acknowledgment_date')
                ).count()

                historical_performance.on_time_delivery_rate = round((on_time_delivery_count / completed_pos) * 100, 2)
                historical_performance.save()
                vendor_model.update(on_time_delivery_rate = historical_performance.on_time_delivery_rate)
                
                       
    @receiver(post_save, sender=PO_Details)
    def update_historical_performance_quality_rating_avg(sender, instance, created, **kwargs):
        if created and instance.status == 'Delivered' and instance.quality_rating is not None:
            vendor = instance.vendor

            historical_performance, created = Historical_Performance.objects.get_or_create(
                vendor=vendor,
                date=date.today()
            )
            vendor_model = Vendor_Details.objects.filter(vendor_name = vendor.vendor_name)
            
            completed_pos = vendor.vendor_set.filter(status='Delivered').count()

            # Avoid division by zero
            if completed_pos > 0:
                historical_performance.quality_rating_avg = (
                    (historical_performance.quality_rating_avg * completed_pos + instance.quality_rating) /
                    (completed_pos + 1)
                )
                historical_performance.save()
                vendor_model.update(quality_rating_avg = historical_performance.quality_rating_avg)

        
 
    @receiver(post_save, sender=PO_Details)
    def update_historical_performance_average_response_time(sender, instance, created, **kwargs):
        if created and instance.acknowledgment_date:
            vendor = instance.vendor

            historical_performance, created = Historical_Performance.objects.get_or_create(
                vendor=vendor,
                date=date.today()
            )
            
            vendor_model = Vendor_Details.objects.filter(vendor_name = vendor.vendor_name)

            response_times = vendor.vendor_set.exclude(acknowledgment_date__isnull=True).values_list(
                'acknowledgment_date', 'issue_date'
            )

            # Calculate average response time
            if response_times:
                average_response_time = sum(
                    (acknowledgment_date - issue_date).total_seconds() for acknowledgment_date, issue_date in response_times
                ) / len(response_times)

                historical_performance.average_response_time = timedelta(seconds=average_response_time)
                historical_performance.save()
                vendor_model.update(average_response_time = historical_performance.average_response_time)

    
    
    @receiver(post_save, sender=PO_Details)
    def calculate_historical_performance_fulfillment_rate(sender, instance, created, **kwargs):
        if created:
            vendor = instance.vendor

            historical_performance, created = Historical_Performance.objects.get_or_create(
                vendor=vendor,
                date=date.today()
            )
            vendor_model = Vendor_Details.objects.filter(vendor_name = vendor.vendor_name)

            total_pos = vendor.vendor_set.filter(status='Delivered').count()

            # Avoid division by zero
            if total_pos > 0:
                successful_pos = vendor.vendor_set.filter(status='Delivered', quality_rating__isnull=False).count()

                historical_performance.fulfillment_rate = round((successful_pos / total_pos) * 100, 2)
                historical_performance.save()
                vendor_model.update(fulfillment_rate = historical_performance.fulfillment_rate)