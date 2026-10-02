
from django.contrib import admin

from apps.collector.models import CollectionAssignment

# Register your models here.
@admin.register(CollectionAssignment)
class CollectionAssignmentAdmin(admin.ModelAdmin):
    list_display = ['collection_request','collector', 'status']
    list_filter = ['collection_request','collector', 'status']
