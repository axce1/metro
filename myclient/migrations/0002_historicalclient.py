# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-28 13:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myclient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalClient',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('tel', models.CharField(blank=True, max_length=30, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=30, verbose_name='Email')),
                ('hide', models.CharField(blank=True, choices=[('no', 'Не скрыт'), ('yes', 'Скрыт')], default='0', max_length=30, verbose_name='Скрыт')),
                ('hide_date', models.DateField(blank=True, null=True, verbose_name='Скрыть до')),
                ('area_ot', models.IntegerField(blank=True, default=0, verbose_name='Площадь от')),
                ('area_do', models.IntegerField(blank=True, default=0, verbose_name='Площадь до')),
                ('price_obsh', models.IntegerField(blank=True, default=0, verbose_name='Цена до')),
                ('price_m', models.IntegerField(blank=True, default=0, verbose_name='Цена до за м2')),
                ('dop_kont', models.TextField(blank=True, max_length=1000, verbose_name='Дополнительные контакты')),
                ('metro', models.BooleanField(max_length=30, verbose_name='У метро')),
                ('adres', models.BooleanField(max_length=100, verbose_name='С адресом')),
                ('komisiya', models.BooleanField(max_length=30, verbose_name='Без комиссии')),
                ('etaj', models.BooleanField(max_length=30, verbose_name='1 этаж')),
                ('podborka', models.BooleanField(max_length=30, verbose_name='Отправить подборку')),
                ('type_obj', models.CharField(blank=True, choices=[('undeg', 'Подземка'), ('street', 'Улица'), ('tc', 'Отдел\\ТЦ')], default='undeg', max_length=30, verbose_name='Тип объекта')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Создан'), ('~', 'Изменен'), ('-', 'Удален')], max_length=1)),
                ('change_message', models.TextField(blank=True, verbose_name='change message')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_client', to=settings.AUTH_USER_MODEL)),
                ('my_manager', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('naznach_one', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='myclient.Naznach')),
                ('naznach_two', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='myclient.Naznach')),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Клиент',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
    ]
