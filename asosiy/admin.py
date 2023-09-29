from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_filter = ["ish_vaqti"]
    search_fields = ["ism"]

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    search_fields = ['ism']
    list_filter = ["tirik"]
    list_display = ["id", "ism", "kitob_soni", "tirik"]
    list_display_links = ["id", "ism"]
    list_editable = ["kitob_soni", "tirik"]



admin.site.register(Talaba)
# admin.site.register(Muallif)
admin.site.register(Kitob)
# admin.site.register(Admin)
admin.site.register(Record)

