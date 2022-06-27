from django.contrib import admin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

from .models import *
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.

admin.site.register(Catalog)
admin.site.register(Brends)
admin.site.register(Collections)
admin.site.register(Colors)
admin.site.register(SocketsCategory)
admin.site.register(CartItem)


class ProductResourse(resources.ModelResource):
    brend_name = fields.Field(column_name="brend_name",attribute="Бренд", widget=ForeignKeyWidget(Product,"name"))
    class Meta:
        model = Product


class ProductAdmin(ImportExportActionModelAdmin):
    resource_class = ProductResourse
    list_display = [field.name for field in Product._meta.fields if field.name != "id"]
    # inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
