from django.contrib import admin
from .models import *

# Register your models here.
class PicAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Pic, PicAdmin)
admin.site.register(Paparazzo)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(tags)