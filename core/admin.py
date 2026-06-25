from django.contrib import admin

from .models import Company, Customer, ServicePlan, Subscription


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "billing_email", "active")
    search_fields = ("name", "slug", "billing_email")
    list_filter = ("active",)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "designation", "phone")
    search_fields = ("user__username", "user__email", "company__name")
    list_filter = ("company",)


@admin.register(ServicePlan)
class ServicePlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price_monthly")
    search_fields = ("name",)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("company", "plan", "active", "paid", "started_at", "expires_at")
    list_filter = ("active", "paid", "plan")
    search_fields = ("company__name",)
