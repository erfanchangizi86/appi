from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    price = models.FloatField(verbose_name="قیمت")
    short_body = models.CharField(verbose_name="توضیحات کوتاه", max_length=300, db_index=True)
    body = models.TextField(db_index=True, verbose_name="توضیحات")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    is_deleted = models.BooleanField(default=False, verbose_name="حذف شده/حذف نشده")