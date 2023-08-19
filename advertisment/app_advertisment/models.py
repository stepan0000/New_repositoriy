from django.db import models
from django.utils.html import format_html
from django.contrib import admin


from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Advertisment(models.Model):
    title = models.CharField("название",max_length=120)
    descriptions = models.TextField("описание")
    price = models.DecimalField("цена",max_digits=9, decimal_places=2)
    trades = models.BooleanField("Торг",help_text="Если хотим торговаться")
    date_now = models.DateTimeField("Создание дата",auto_now_add= True)
    date_update = models.DateTimeField("Обновление дата", auto_now= True)
    image = models.ImageField("Картинка",upload_to='advertisments/')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = "Advertisment"

    def __str__(self):
        return self.title
    

    @admin.display(description = "Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.date_now.date() == timezone.now().date():
            created_time = self.date_now.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color:green; font-weight: bold;">Сегодня в {}</span>',created_time
            )
        return self.date_now.strftime("%d.%m.%Y  в  %H:%M:%S")


    
    @admin.display(description = "картинка")
    def created_foto(self):
        if self.image:
            return format_html(
                '<img src = "/media/{}" style = "width:100px; hight:100px;"> ',self.image
            )
        else:
            return format_html(
                '<img src = "/static/img/adv.png" style = "width:100px; hight:100px;"> '
            )
       