# Generated by Django 3.1.2 on 2020-11-11 17:50

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceName', models.CharField(max_length=20, null=True, verbose_name='نوع الجهاز')),
                ('kind', models.CharField(max_length=20, null=True, verbose_name='النوع')),
                ('raterName', models.CharField(max_length=20, null=True, verbose_name='إسم المقيم')),
                ('raterid', models.IntegerField(null=True, verbose_name='المقيم')),
                ('rate', models.FloatField(null=True, verbose_name='التقييم')),
                ('date', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='التاريخ')),
                ('time', models.TimeField(default=django.utils.timezone.now, null=True, verbose_name='الوقت')),
            ],
        ),
        migrations.CreateModel(
            name='QuerrySellers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfMandoop', models.CharField(choices=[('فايز', 'وليد'), ('فايز', 'فايز'), ('حسن', 'حسن'), ('إبراهيم', 'إبراهيم'), ('خط دكرنس', 'خط دكرنس')], max_length=50, verbose_name='إسم المندوب')),
                ('area', models.CharField(choices=[('نبروه', 'نبروه'), ('بلقاس', 'بلقاس')], max_length=50, verbose_name='المنطقة')),
                ('activityKind', models.CharField(choices=[('سنترال وخدمات محمول', 'سنترال وخدمات محمول'), ('خدمات كمبيوتر', 'خدمات كمبيوتر'), ('عطارة', 'عطارة'), ('مكتبة', 'مكتبة'), ('بقالة', 'بقالة'), ('سوبر ماركت', 'سوبر ماركت'), ('other', 'أخر: ')], max_length=20, null=True, verbose_name='نوع النشاط ')),
                ('shopName', models.CharField(max_length=50, null=True, verbose_name='إسم المحل ')),
                ('ownerName', models.CharField(max_length=50, null=True, verbose_name='إسم صاحب العمل ')),
                ('phoneNumber', models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[0-9+]', 'Only digit characters.')], verbose_name='رقم التليفون ')),
                ('address', models.TextField(max_length=100, null=True, verbose_name='العنوان بالتفصيل ')),
                ('machinesOfepay', models.CharField(choices=[('امان', 'امان'), ('فورى', 'فورى'), ('بى', 'بى'), ('مصارى', 'مصارى'), ('ضامن', 'ضامن'), ('سداد', 'سداد')], max_length=20, null=True, verbose_name='مكن الدفع الإلكترونى ')),
                ('tayer', models.CharField(choices=[('يوجد', 'يوجد'), ('لا يوجد', 'لا يوجد')], max_length=20, null=True, verbose_name='الطاير ')),
                ('intention', models.CharField(max_length=100, null=True, verbose_name='ما مدى قابليته للتعامل معنا')),
                ('amountOfTreat', models.CharField(choices=[('اقل من 10 الاف', 'اقل من 10 الاف'), ('من 10 الاف ل 25000', 'من 10 الاف ل 25000'), ('من 25 الف ل 50 الف', 'من 25 الف ل 50 الف'), ('اعلي من 50 الف', 'اعلي من 50 الف')], max_length=20, null=True, verbose_name='حجم التعامل ')),
                ('kindOfMobile', models.CharField(choices=[('سامسونج', 'سامسونج'), ('هواوى', 'هواوى'), ('أبل', 'أبل'), ('شاومى', 'شاومى'), ('نوكيا', 'نوكيا'), ('انفنكس', 'انفنكس'), ('أوبو', 'أوبو')], max_length=20, null=True, verbose_name='نوع اجهزه المحمول')),
                ('sim', models.CharField(choices=[('فودافون', ' فودافون'), ('إتصالات', 'إتصالات'), ('أورنج', 'أورنج')], max_length=20, null=True, verbose_name='الكارت')),
                ('evaluate', models.CharField(choices=[('مهم', 'مهم'), ('مهم جدا', 'مهم جدا'), ('متوسط', 'متوسط'), ('غير مهم', 'غير مهم')], max_length=20, null=True, verbose_name='التقييم')),
                ('notes', models.TextField(max_length=100, null=True, verbose_name='الملاحظات')),
                ('date', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='التاريخ')),
                ('time', models.TimeField(default=django.utils.timezone.now, null=True, verbose_name='الوقت')),
                ('addressmap', django_google_maps.fields.AddressField(max_length=200, null=True)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100, null=True)),
            ],
        ),
    ]
