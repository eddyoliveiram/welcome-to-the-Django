from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group

from .models import Post, Comment


# Unregister default User and Group admin
admin.site.unregister(User)
admin.site.unregister(Group)


# Customize User Admin
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        # Add groups field to the last fieldset
        fieldsets = list(fieldsets)
        if fieldsets:
            last_fieldset = list(fieldsets[-1])
            last_fieldset[1]['fields'] = tuple(list(last_fieldset[1]['fields']) + ['groups'])
            fieldsets[-1] = tuple(last_fieldset)
        return fieldsets


# Customize Group Admin
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_permissions_count')
    filter_horizontal = ('permissions',)
    
    def get_permissions_count(self, obj):
        return obj.permissions.count()
    get_permissions_count.short_description = 'Permissões'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Informações do Post', {
            'fields': ('title', 'content', 'author')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('created_at', 'author', 'post')
    search_fields = ('content', 'author__username', 'post__title')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Informações do Comentário', {
            'fields': ('post', 'author', 'content')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
