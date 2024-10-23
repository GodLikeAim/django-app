from django.contrib import admin
from .models import Contact
from .models import About

admin.site.register(About)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    class Meta:
        model = Contact

