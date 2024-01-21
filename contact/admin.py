from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)
    list_display = ('name', 'subject', 'created_on', 'responded',)
    list_editable = ('responded',)
    order = ('-created_on')


admin.site.register(Contact, ContactAdmin)