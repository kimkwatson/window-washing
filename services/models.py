from django.db import models

class ServiceRequest(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)

    windows = models.IntegerField()

    SERVICE_CHOICES = [
        ("inside", "Inside"),
        ("outside", "Outside"),
        ("both", "Inside & Outside"),
    ]

    service = models.CharField(max_length=10, choices=SERVICE_CHOICES)

    day = models.DateField()

    notes = models.TextField(blank=True)
    
    completed = models.BooleanField(default=False)
    
    paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fname} {self.lname} - {self.day}"
