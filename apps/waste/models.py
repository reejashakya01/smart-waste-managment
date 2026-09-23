from django.db import models

# Create your models here.
class WasteCategory(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)
    description = models.TextField()
    is_recyclable = models.BooleanField(default=False)
    base_rate = models.DecimalField(max_digits=5, decimal_places=2)
    reward_points_per_kg = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "waste_category"