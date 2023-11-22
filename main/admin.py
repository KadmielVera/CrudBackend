from django.contrib import admin
from .models import Crud


class DetDefault(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10


admin.site.register(Crud, DetDefault)


