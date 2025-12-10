from django.db import models

# Create your models here.

class Supplier(models.Model):
    # Verification
    verification_code = models.CharField(max_length=10, blank=True, null=True)

    # Company Info
    company_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    company_type = models.CharField(max_length=100)
    website = models.URLField()

    # Contact Info
    sales_name = models.CharField(max_length=100)
    email = models.EmailField()
    country_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    # Product & Services
    categories = models.JSONField()
    other_category = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=200)

    catalog_url = models.URLField(blank=True, null=True)
    catalog_files = models.JSONField(blank=True, null=True)

    moq = models.CharField(max_length=50)

    # Certifications
    certifications = models.JSONField(blank=True, null=True)
    other_certs = models.CharField(max_length=255, blank=True, null=True)

    # Buyer Intent
    buyer_intent = models.JSONField(blank=True, null=True)

    # Consent
    consent = models.BooleanField(default=False)

    # Auto
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
