from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from basic_app import models


# Register your models here.
class CustomUserAdmin(UserAdmin):
    ordering = ('is_superuser',)
    search_fields = ('username',)
    list_filter = ('username',)
    list_display = ('username', 'is_superuser', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password', 'is_superuser', 'is_staff', 'is_active')}),
        ('Permissions', {'fields': ('groups',)}),
        ('Group Permissions', {'classes': ('collapse',), 'fields': ('user_permissions',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active')
        }),
    )


admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.LogoName)
admin.site.register(models.Home)
admin.site.register(models.Blog)
admin.site.register(models.Form)
admin.site.register(models.Product)
admin.site.register(models.AboutProduct)
admin.site.register(models.ContactLocation)
admin.site.register(models.ProductType)
admin.site.register(models.AboutPricing)
admin.site.register(models.Award)
admin.site.register(models.SecondBlog)
