# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-28 13:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myobject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalMyObject',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('typeobj', models.CharField(choices=[('1', 'Павильон'), ('2', 'Капитальное'), ('3', 'Отдел\\БЦ\\ТЦ'), ('4', 'Подземка')], default='0', max_length=30, verbose_name='Тип объекта')),
                ('adres', models.CharField(max_length=100, verbose_name='Адрес')),
                ('area', models.IntegerField(default=0, verbose_name='Площадь')),
                ('block_area', models.FloatField(blank=True, default=0, verbose_name='Метраж')),
                ('block_price', models.FloatField(blank=True, default=0, verbose_name='Цена')),
                ('block_procent', models.FloatField(blank=True, default=0, verbose_name='Процент комиссии')),
                ('etaj', models.IntegerField(blank=True, default=0, verbose_name='Этаж')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('opis', models.TextField(blank=True, max_length=1000, verbose_name='Описание')),
                ('dom', models.BooleanField(default=False, verbose_name='Дом')),
                ('kvt', models.CharField(blank=True, max_length=50, verbose_name='КВт')),
                ('dogovor', models.CharField(blank=True, max_length=50, verbose_name='Тип договора')),
                ('block_name', models.CharField(blank=True, max_length=20, verbose_name='Имя')),
                ('block_tel', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('block_email', models.EmailField(blank=True, max_length=30, verbose_name='Email')),
                ('silka', models.CharField(blank=True, max_length=200, verbose_name='Ссылка на сайт')),
                ('zametka', models.TextField(blank=True, max_length=1000, verbose_name='Заметка')),
                ('hide', models.CharField(blank=True, choices=[('no', 'Нет'), ('yes', 'Все')], default='0', max_length=30, verbose_name='Скрыт')),
                ('hide_date', models.DateField(blank=True, null=True, verbose_name='Скрыть до')),
                ('zvon', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Скрыть до')),
                ('area_range', models.CharField(blank=True, choices=[('small', 'Маленькое до 20 кв.м'), ('middle', 'Среднее от 20 до 80 кв.м'), ('large', 'Большое до 80 кв.м')], max_length=50, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Создан'), ('~', 'Изменен'), ('-', 'Удален')], max_length=1)),
                ('change_message', models.TextField(blank=True, verbose_name='change message')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_object', to=settings.AUTH_USER_MODEL)),
                ('my_manager', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('station_one', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='myobject.StancMetro')),
                ('station_two', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='myobject.StancMetro')),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Объект',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
    ]
