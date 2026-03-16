from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):

    def customer_name(self, obj):
        return f"{obj.fname} {obj.lname}"
    
    customer_name.short_description = "Customer"

    list_display = ("customer_name", "city", "windows", "service", "day", "created_at")
    ordering = ("-created_at",)
    search_fields = ("name", "city")
    list_filter = ("service", "day")

admin.site.register(ServiceRequest, ServiceRequestAdmin)

admin.site.site_header = "Window Washing Admin Console"
admin.site.site_title = "Window Washing Admin"
admin.site.index_title = "Service Request Management"
