from django.contrib import admin
from .models import Item, ItemImage, Category, Label

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



# admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Category)
admin.site.register(Label)