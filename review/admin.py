from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)
    list_display = (
        'user', 'content', 'created_on', 'is_approved', 'homepage',)
    list_editable = ('is_approved',  'homepage',)
    order = ('-created_on')


admin.site.register(Review, ReviewAdmin)
