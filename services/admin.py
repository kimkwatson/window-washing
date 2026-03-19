from django.contrib import admin
from .models import ServiceRequest

class CompletionFilter(admin.SimpleListFilter):
    title = "Completion status"
    parameter_name = "completion"

    def lookups(self, request, model_admin):
        return (
            ("incomplete", "Incomplete"),
            ("complete", "Completed"),
        )

    def queryset(self, request, queryset):
        if self.value() == "incomplete":
            return queryset.filter(completed=False)
        if self.value() == "complete":
            return queryset.filter(completed=True)

class ServiceRequestAdmin(admin.ModelAdmin):

    def customer_name(self, obj):
        return f"{obj.fname} {obj.lname}"
    
    customer_name.short_description = "Customer"

    list_display = ("customer_name", "city", "windows", "service", "day", "completed", "paid", "created_at")
    list_editable = ("completed", "paid")
    ordering = ("-created_at",)
    search_fields = ("name", "city")
    list_filter = (CompletionFilter, "service", "day", "paid")

admin.site.register(ServiceRequest, ServiceRequestAdmin)

admin.site.site_header = "Window Washing Admin Console"
admin.site.site_title = "Window Washing Admin"
admin.site.index_title = "Service Request Management"
