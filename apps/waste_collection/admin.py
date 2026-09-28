from django.contrib import admin

from apps.waste_collection.models import (
    CollectionRequest,
    CollectionRequestItem,
    CollectionActivity,
)


@admin.register(CollectionRequest)
class CollectionRequestAdmin(admin.ModelAdmin):
    list_display = (
        "request_number",
        "user",
        "scheduled_date",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "scheduled_date",
        "created_at",
    )

    search_fields = (
        "request_number",
        "user__email",
        "user__username",
        "user__first_name",
        "user__last_name",
    )

    readonly_fields = (
        "request_number",
        "created_at",
        "updated_at",
    )

    date_hierarchy = "scheduled_date"

    ordering = ("-created_at",)

    list_per_page = 25

@admin.register(CollectionRequestItem)
class CollectionRequestItemAdmin(admin.ModelAdmin):
    list_display = (
        "collection_request",
        "waste_category",
        "estimated_quantity",
        "actual_quantity",
        "unit",
        "estimated_amount",
        "actual_amount",
        "reward_points",
    )

    list_filter = ("unit",)

    search_fields = (
        "collection_request__request_number",
    )

    autocomplete_fields = (
        "collection_request",
        "waste_category",
    )

    list_per_page = 25


@admin.register(CollectionActivity)
class CollectionActivityAdmin(admin.ModelAdmin):
    list_display = (
        "collection",
    )

    search_fields = (
        "collection__request_number",
    )

    autocomplete_fields = (
        "collection",
    )

    list_per_page = 25
    
    
    def has_delete_permission(self, request, obj = ...):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj = ...):
        return False