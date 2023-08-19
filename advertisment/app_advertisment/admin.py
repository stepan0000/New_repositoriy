from django.contrib import admin
from .models import Advertisment
# Register your models here.
class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ['title','descriptions','price','trades','date_now',"created_date",'image','created_foto','user']
    list_filter = ['date_now','descriptions',"trades"]
    fieldsets =(
        ("Первый блок",{
            "fields":("title","descriptions",'image','user')}),

        ("Второй блок",{
            'classes': ('collapse',),
            "fields":('price','trades')}),
        )
    
    actions = ['make_true','make_False','created_date']
    @admin.action(description="Обновить торг на True")
    def make_true(self,request,queryset):
        queryset.update(trades = True)

    @admin.action(description="Обновить торг на False")
    def make_False(self,request,queryset):
        queryset.update(trades = False)
        

admin.site.register(Advertisment,AdvertismentAdmin)















# @admin.register(Advertisment) # admin.site.register(Advertisment,AdvertismentAdmin)
# class AdvertismentAdmin(admin.ModelAdmin):
#     list_display = ['id','title','descriptions','price',"date_now",'trades','date_update',"created_date"]
#     list_filter = ['date_now','descriptions',"trades"]
#     fieldsets =(
#         ("Первый блок",{
#             "fields":("title","descriptions")}),
#         ("Второй блок",{
            
#             'classes': ('collapse',),
#             "fields":('price','trades')}),
#         )
#     actions =["make_auctio_as_false","make_auctio_as_true"]
        
#     @admin.action(description="Убрать возможность торга")
#     def make_auctio_as_false(self,request,queryset):
#         queryset.update(trades = False)
#     @admin.action(description="Поставить торг")
#     def make_auctio_as_true(self,request,queryset):
#         queryset.update(trades = True)
    # actions_selection_counter = False
    
    # fields = ('title', 'trades')


    # actions_on_bottom = False
    # actions_on_top = True