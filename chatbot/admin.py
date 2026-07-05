from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "name",
        "email",
        "phone",
        "requirement",
        "status",
        "source",
    )
    list_filter = ("status", "source", "created_at")
    search_fields = ("name", "email", "phone", "requirement", "message")
    ordering = ("-created_at",)