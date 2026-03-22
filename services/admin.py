from django.contrib import admin
from .models import ServiceRequest

# custom filter for the admin sidebar to show completed vs incomplete jobs
class CompletionFilter(admin.SimpleListFilter):
    title = "Completion status"
    parameter_name = "completion"

    # options that appear in the filter dropdown
    def lookups(self, request, model_admin):
        return (
            ("incomplete", "Incomplete"),
            ("complete", "Completed"),
        )

    # what happens when a filter is selected
    def queryset(self, request, queryset):
        if self.value() == "incomplete":
            return queryset.filter(completed=False)
        if self.value() == "complete":
            return queryset.filter(completed=True)

class ServiceRequestAdmin(admin.ModelAdmin):

    # combine first and last name into one column
    def customer_name(self, obj):
        return f"{obj.fname} {obj.lname}"
    
    # rename column header in admin
    customer_name.short_description = "Customer"

    # columns shown in the admin list view
    list_display = ("customer_name", "city", "windows", "service", "day", "completed", "paid", "created_at")
    # fields that can be edited directly from list view
    list_editable = ("completed", "paid")
    # order records by newest first
    ordering = ("-created_at",)
    # search bar fields
    search_fields = ("name", "city")
    # filters shown in sidebar
    list_filter = (CompletionFilter, "service", "day", "paid")

# register model with custom admin configuration
admin.site.register(ServiceRequest, ServiceRequestAdmin)

# customize admin page titles
admin.site.site_header = "Window Washing Admin Console"
admin.site.site_title = "Window Washing Admin"
admin.site.index_title = "Service Request Management"
