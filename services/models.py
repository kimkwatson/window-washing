from django.db import models

class ServiceRequest(models.Model):

    # customer info
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)

    # address info
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)

    # job details
    stories = models.IntegerField()
    windows = models.IntegerField()

    # valid service types in database
    SERVICE_CHOICES = [
        ("inside", "Inside"),
        ("outside", "Outside"),
        ("both", "Inside & Outside"),
    ]

    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)

    day = models.DateField()

    notes = models.TextField(blank=True)
    
    # admin tracking fields
    completed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    # auto set date when request is created
    created_at = models.DateTimeField(auto_now_add=True)

    # how object is displayed in admin interface
    def __str__(self):
        return f"{self.fname} {self.lname} - {self.day}"
