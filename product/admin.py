from django.contrib import admin
from product.models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product
    search_fields = ['title', 'descriptions']
    list_display = 'id title category price'.split()
    list_filter = 'category'.split()


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Review)
