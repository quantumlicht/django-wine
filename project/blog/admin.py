from django.contrib import admin
from .models import BlogEntry, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class BlogEntryAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(BlogEntry, BlogEntryAdmin)


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['author', 'content']
    list_display = ('author', 'pub_date', 'blogEntry')
    list_filter = ['author', 'pub_date', 'content']
admin.site.register(Comment, CommentAdmin)
