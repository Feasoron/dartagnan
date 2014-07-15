from django.contrib import admin
from dartagnan.menu.models import Category, MenuItem


class MenuItemsInline(admin.TabularInline):
    model = MenuItem
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
        fieldsets = [
            (None, {'fields': ['title']}),
        ]
        inlines = [MenuItemsInline]


admin.site.register(Category, CategoryAdmin)