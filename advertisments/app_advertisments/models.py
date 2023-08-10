from django.db import models
from django.utils.html import format_html
from django.contrib import admin   
# Create your models here.
class Advertisment(models.Model):
    title = models.CharField("название",max_length=120)
    descriptions = models.TextField("описание")
    price = models.DecimalField("цена",max_digits=9,decimal_places=2)
    trades = models.BooleanField("торг",help_text="Если хотим торговаться")
    date_now = models.DateTimeField("Создание дата",auto_now_add= True)
    date_update = models.DateTimeField("Обновление дата",auto_now = True)
    class Meta:
        db_table = "advertisments"
    def __str__(self):
        return f"id={self.pk},title={self.title},price={self.price}"
    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.date_now.date() == timezone.now().date():
            created_time = self.date_now.time().strftime("%H%M:%S")
            return format_html(
                '<span style = "color:green;font-weight: bold;">Сегодня в {}</span>',created_time
            )
        return self.date_now.strftime("%d.%m.%Y в %H:%M:%S" )
    @admin.display(description="Дата обновления")
    def updated_date(self):
        from django.utils import timezone
        if self.date_update.date() == timezone.now().date():
            updated_time = self.date_update.time().strftime("%H%M:%S")
            return format_html(
                '<span style = "color:red;font-weight: bold;">Сегодня в {}</span>',updated_time
            )
        return self.date_now.strftime("%d.%m.%Y в %H:%M:%S")