from django.contrib import admin

from .models import NewsItem

# Register your models here.
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "content")
    search_fields = ("title", "date")


admin.site.register(NewsItem, NewsItemAdmin)
