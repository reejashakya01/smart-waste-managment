from django.db import models

from apps.accounts.models import Role, User
from apps.waste_collection.models import CollectionRequest

class CollectionAssignmentStatus(models.TextChoices):
    ASSIGNED = "assigned"
    ACCEPTED = "accepted"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"
    REJECTED = "rejected"
    PENDING = "pending"

# Create your models here.
class CollectionAssignment(models.Model):
    collection_request = models.ForeignKey(CollectionRequest, on_delete=models.CASCADE)
    collector = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": Role.COLLECTOR}
    )
    status = models.CharField(
        max_length=20,
        choices=CollectionAssignmentStatus.choices,
        default=CollectionAssignmentStatus.PENDING,
    )
    assigned_at = models.DateTimeField(null=True, blank=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "collection-assignment"

    def __str__(self):
        return f"{self.collection_request} - {self.collector} - {self.status}"