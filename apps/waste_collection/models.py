from django.db import models
from apps.accounts.models import User
from apps.waste.models import WasteCategory, WasteUnit

# Create your models here.
class CollectionRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    request_number = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    scheduled_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.request_number

    class Meta:
        db_table = "collection-request"
        
class CollectionRequestItem(models.Model):
    collection_request = models.ForeignKey(CollectionRequest, on_delete=models.RESTRICT)
    waste_category = models.ForeignKey(
        WasteCategory, on_delete=models.SET_NULL, null=True
    )
    estimated_quantity = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    actual_quantity = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    unit = models.CharField(max_length=5, choices=WasteUnit.choices)
    estimated_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    actual_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    reward_points = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f"{self.collection_request.request_number} - {self.waste_category}"

    class Meta:
        db_table = "collection-item"


class CollectionActivity(models.Model):
    collection = models.ForeignKey(
        CollectionRequest, on_delete=models.SET_NULL, null=True)