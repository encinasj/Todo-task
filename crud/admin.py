from django.contrib import admin

from .models import Crud

class CrudAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(Crud, CrudAdmin)