from django.contrib import admin
from .models import project_page


class project_page_admin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_per_page = 20
    list_display_links = ('title',)


admin.site.register(project_page,project_page_admin)
# Register your models here.
