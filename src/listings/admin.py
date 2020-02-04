from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display       = ('id', 'title', 'is_punlished','price','list_date', 'realtor')
    list_display_links =('id', 'title')
    list_filter        = ('realtor', )
    list_editable      = ('is_punlished', )
    search_fields      = ('title', 'description', 'address', 'city','county', 'price')
    list_per_page      = 25

admin.site.register(Listing, ListingAdmin)
