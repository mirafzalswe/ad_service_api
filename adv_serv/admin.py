from django.contrib import admin

# Register your models here.
from .models import Ad

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'ad_id', 'author', 'views', 'position')
    search_fields = ('title', 'author')
    list_filter = ('author',)
