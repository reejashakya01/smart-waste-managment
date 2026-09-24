from django.contrib import admin

# Register your models here.
from .models import WasteCategory


@admin.register(WasteCategory)
class WasteCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "is_recyclable",
        "base_rate",
        "reward_points_per_kg",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_recyclable",
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "code",
        "description",
    )

    ordering = ("name",)

    list_per_page = 25

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "code",
                    "description",
                )
            },
        ),
        (
            "Waste & Reward Configuration",
            {
                "fields": (
                    "is_recyclable",
                    "base_rate",
                    "reward_points_per_kg",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )
    
from django.contrib import admin

from .models import WasteMaterial


@admin.register(WasteMaterial)
class WasteMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "unit",
        "estimated_rate",
        "is_active",
    )

    list_filter = (
        "unit",
        "is_active",
        "category",
    )

    search_fields = (
        "category__name",
    )

    list_editable = (
        "estimated_rate",
        "is_active",
    )

    ordering = (
        "category__name",
    )

    list_per_page = 25