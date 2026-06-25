from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    website = models.URLField(blank=True)
    billing_email = models.EmailField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ServicePlan(models.Model):
    name = models.CharField(max_length=128)
    price_monthly = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    features = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.name} (${self.price_monthly}/mo)"


class Subscription(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="subscriptions")
    plan = models.ForeignKey(ServicePlan, on_delete=models.PROTECT)
    started_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    active = models.BooleanField(default=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company.name} - {self.plan.name}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="customers")
    designation = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
