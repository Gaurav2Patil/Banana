from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin 

# Register your models here.
admin.site.register(Carousel)
admin.site.register(Interior_products)
admin.site.register(Exterior_products)
admin.site.register(Base_paint_products)
admin.site.register(Blogs)
admin.site.register(Colors,ImportExportActionModelAdmin)
admin.site.register(Contacts,ImportExportActionModelAdmin)