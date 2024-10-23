from django.contrib import admin
from .models import Article, Comment, FooterSettings, Service

# Register your models here.
# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date", 'is_approved']
    list_display_links = ["title", "created_date"]
    search_fields = ["title", 'is_approved']
    list_filter = ["created_date", 'is_approved']
    class Meta:
        model = Article

# from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'content', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('content', 'author__username')

# from .models import FooterSettings

admin.site.register(FooterSettings)

# from .models import Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    search_fields = ('title',)
    readonly_fields = ('created_date',)