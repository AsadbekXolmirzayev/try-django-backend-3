from django.contrib import admin
from .models import Article

# admin.site.register(Article)

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_deleted', 'modefied_date', 'created_date']
    readonly_fields = ['modefied_date', 'created_date']
    fields = ['title', 'image', 'content', 'modefied_date', 'created_date']
    list_display_links = ('title', 'id',)
    list_per_page = 10
    ordering = ('id',)
    search_fields = ('title', )
    search_help_text = "title' orqali qidiradi"
    list_filter = ('is_deleted', 'created_date', 'modefied_date',)
    date_hierarchy = "created_date"

admin.site.register(Article, ArticleAdmin)