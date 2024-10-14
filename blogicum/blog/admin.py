from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_published', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'pub_date', 'is_published')
    search_fields = ('title', 'text', 'author__username')
    list_filter = ('is_published', 'pub_date', 'category', 'location')
    autocomplete_fields = ('author', 'category', 'location')


if admin.site.is_registered(Group):
    admin.site.unregister(Group)
