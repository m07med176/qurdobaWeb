# Generated by Django 3.1.2 on 2020-11-02 15:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querriesTraders', '0002_auto_20201102_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querrysellers',
            name='activityKind',
            field=models.CharField(choices=[('a', 'سنترال وخدمات محمول'), ('b', 'خدمات كمبيوتر')], max_length=20, null=True, verbose_name='نوع النشاط '),
        ),
        migrations.AlterField(
            model_name='querrysellers',
            name='address',
            field=models.TextField(max_length=100, null=True, verbose_name='العنوان بالتفصيل '),
        ),
        migrations.AlterField(
            model_name='querrysellers',
            name='amountOfTreat',
            field=models.CharField(choices=[('a', 'اقل من 10 الاف'), ('b', 'من 10 الاف ل 25000'), ('c', 'من 25 الف ل 50 الف'), ('d', 'اعلي من 50 الف')], max_length=20, null=True, verbose_name='حجم التعامل '),
        ),
        migrations.AlterField(
            model_name='querrysellers',
            name='evaluate',
            field=models.CharField(choices=[('a', 'مهم'), ('b', 'مهم جدا'), ('c', 'متوسط'), ('d', 'غير مهم')], max_length=20, null=True, verbose_name='التقييم'),
        ),
        migrations.AlterField(
            model_name='querrysellers',
            name='kindOfMobile',
            field=models.CharField(choices=[('a', 'سامسونج'), ('b', 'هواوى'), ('c', 'أبل'), ('d', 'شاومى'), ('e', 'نوكيا'), ('f', 'انفنكس'), ('g', 'أوبو')], max_length=20, null=True, verbose_name='نوع اجهزه المحمول'),
        ),
        migrations.AlterField(
            model_name='querrysellers',
            name='machinesOfepay',
            field=models.CharField(choices=[('a', 'امان'), ('b', 'فورى'), ('c', 'بى'), ('d', 'مصارى'), ('e', 'ضامن'), ('f', 'سداد')], max_length=20, null=True, verbose_name='مكن الدفع الإلكترونى '),
        ),
        migrations.AlterField(
            model_name='querrysellers',
            name='notes',
            field=models.TextField(max_length=100, null=True, verbose_name='الملاحظات'),
        ),
        migrations.AlterField(
            model_name='querrysellers',
            name='ownerName',
            field=models.CharField(max_length=50, null=True, verbose_name='إسم صاحب العمل '),
        ),
        migrations.AlterField(
            model_name='querrysellers',
            name='phoneNumber',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[0-9+]', 'Only digit characters.')], verbose_name='رقم التليفون '),
        ),
        migrations.AlterField(
            model_name='querrysellers',
            name='shopName',
            field=models.CharField(max_length=50, null=True, verbose_name='إسم المحل '),
        ),
        migrations.AlterField(
            model_name='querrysellers',
            name='tayer',
            field=models.CharField(choices=[('a', 'يوجد'), ('b', 'لا يوجد')], max_length=20, null=True, verbose_name='الطاير '),
        ),
    ]
