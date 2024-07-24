# Generated by Django 5.0.7 on 2024-07-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='عنوان')),
                ('price', models.FloatField(verbose_name='قیمت')),
                ('short_body', models.CharField(db_index=True, max_length=300, verbose_name='توضیحات کوتاه')),
                ('body', models.TextField(db_index=True, verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='حذف شده/حذف نشده')),
            ],
        ),
    ]
