from django.db import models
# Create your models here.
class Advertisment(models.Model):
    title = models.CharField("название",max_length=120)
    descriptions = models.TextField("описание")
    price = models.DecimalField("цена",max_digits=9,decimal_places=2)
    trades = models.BooleanField("торг",help_text="Если хотим торговаться")
    date_now = models.DateField("Создание дата",auto_now_add= True)
    date_update = models.DateField("Обновление дата",auto_now = True)
    class Meta:
        db_table = "advertisments"
    def __str__(self):
        return f"id={self.pk},title={self.title},price={self.price}"