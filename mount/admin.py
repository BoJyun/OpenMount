from django.contrib import admin
from mount.models import Mount

# Register your models here.

#@admin.register(Mount)
class MountAdmin(admin.ModelAdmin):
   list_display=('id','title')

admin.site.register(Mount, MountAdmin)