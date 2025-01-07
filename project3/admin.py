from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'updated_date',]
    list_filter = ['status',]
    ordering = ['published_date']
    search_fields = ['title', 'content']



admin.site.register(Post, PostAdmin)


# Register your models here.
