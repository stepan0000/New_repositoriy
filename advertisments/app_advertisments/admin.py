from django.contrib import admin 
# Register your models here.
from .models import Advertisment
class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ['title','descriptions','price','trades','date_now','date_update','created_date','updated_date']
    list_filter = ['date_now','descriptions','trades']
    fieldsets = (
        ("Первый блок",{"fields":("title","descriptions")}),
        ("Второй блок",{"fields":("price","trades")}),
    )
    actions = ['make_false','created_date']
    @admin.action(description='Обновить торг на False')
    def make_false(self,request,querysets):
        querysets.update(trades = False)
        pass
admin.site.register(Advertisment,AdvertismentAdmin)