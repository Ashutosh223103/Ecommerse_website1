from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Contact,PropertyListing,seller,buyer,producat
admin.site.site_header = "KEY2HOME administration"
from .models import (
 Customer,
 Product,
 Cart,
 OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'title', 'selling_price', 'discounted_price',  'description', 'brand', 'category', 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user', 'product', 'quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user', 'customer', 'customer_info', 'product', 'product_info', 'quantity', 'ordered_date', 'status']

 def product_info(self, obj):
  link = reverse("admin:app_product_change", args=[obj.product.pk])
  return format_html('<a href="{}">{}</a>', link, obj.product.title)

 def customer_info(self, obj):
  link = reverse("admin:app_customer_change", args=[obj.customer.pk])
  return format_html('<a href="{}">{}</a>', link, obj.customer.name)
 



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email', 'phone', 'address')

admin.site.register(Contact, ContactAdmin)
@admin.register(PropertyListing)
class PropertyListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'city', 'state')
    list_filter = ('bedrooms', 'bathrooms', 'city', 'state')
    search_fields = ('title', 'description', 'address', 'city', 'state', 'country', 'zipcode')

    fieldsets = (
        (None, {
            'fields': ('owner', 'title', 'description', 'price', 'image')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'address', 'city', 'state', 'country', 'zipcode')
        }),
    )

    readonly_fields = ('owner',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        super().save_model(request, obj, form, change)
admin.site.register(seller)
admin.site.register(buyer)
admin.site.register(producat)