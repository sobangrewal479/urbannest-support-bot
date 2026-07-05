from django.core.exceptions import ValidationError
from django.db import models


class Lead(models.Model):
    STATUS_CHOICES = [
        ("New", "New"),
        ("Contacted", "Contacted"),
        ("Closed", "Closed"),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    requirement = models.CharField(max_length=200)
    message = models.TextField()
    preferred_contact_time = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=100, default="Website AI Bot")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="New")
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.email and not self.phone:
            raise ValidationError("Please provide either email or phone number.")

    def __str__(self):
        return f"{self.name} - {self.requirement}"