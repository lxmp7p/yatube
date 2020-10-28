from django.contrib import admin
from .models import Post
from .models import Group

class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
admin.site.register(Post, PostAdmin)

class GroupsList(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description',)
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'
admin.site.register(Group, GroupsList)
