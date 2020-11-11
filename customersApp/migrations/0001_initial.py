# Generated by Django 3.1.2 on 2020-11-11 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sellerName', models.CharField(max_length=50, verbose_name='إسم المندوب')),
                ('region', models.CharField(max_length=20, null=True, verbose_name='المنطقة')),
                ('phoneno', models.IntegerField(null=True, verbose_name='رقم التليفون')),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='الإسم')),
                ('kindshop', models.CharField(choices=[('a', 'بقالة'), ('b', 'منظفات'), ('c', 'سنترال'), ('d', 'صيانة محمول'), ('e', 'إكسسوارات محمول'), ('f', 'أدوات صحية'), ('g', 'مكتبة'), ('h', 'خردوات'), ('y', 'شخصى')], max_length=30, null=True, verbose_name='نوع المحل')),
                ('nameshop', models.CharField(max_length=30, null=True, verbose_name='إسم المحل')),
                ('phoneno', models.IntegerField(null=True, verbose_name='رقم التليفون')),
                ('idno', models.IntegerField(null=True, verbose_name='الرقم القومى')),
                ('address', models.TextField(max_length=100, null=True, verbose_name='العنوان')),
                ('date', models.DateField(max_length=11, null=True, verbose_name='تاريخ التسجيل')),
                ('cardImageFront', models.ImageField(null=True, upload_to='UserImages/cards', verbose_name='صورة البطاقة وجه')),
                ('cardImageBack', models.ImageField(null=True, upload_to='UserImages/cards', verbose_name='صورة البطاقة ظهر')),
                ('proofImage', models.ImageField(null=True, upload_to='UserImages/attached', verbose_name='صور وصل')),
                ('servicekind', models.CharField(choices=[('a', 'ماكينة'), ('b', 'تطبيق')], max_length=30, null=True, verbose_name='نوع الخدمة')),
                ('accountNo', models.IntegerField(null=True, verbose_name='رقم الحساب')),
                ('deviceserial', models.CharField(max_length=50, null=True, verbose_name='سيريال الجهاز')),
                ('servicestate', models.CharField(choices=[('a', 'مفعلة'), ('b', 'غير مفعلة'), ('c', 'موقوفة')], max_length=30, null=True, verbose_name='حاله الخدمة')),
                ('kindmachine', models.CharField(choices=[('a', '520 C زيرو'), ('b', '520 C كسر'), ('c', '520 Contact زيرو'), ('d', '520 Contact كسر'), ('e', '520 Contact زيرو بدون بطارية'), ('f', '520 Contact كسر بدون بطارية')], max_length=30, null=True, verbose_name='نوع الجهاز')),
                ('kindphone', models.CharField(choices=[('a', 'فودافون'), ('b', 'اورنج'), ('c', 'إتصالات'), ('d', 'فودافون + أورنج'), ('e', 'فودافون + إتصالات'), ('f', 'أورنج + فودافون'), ('g', 'أورنج + إتصالات'), ('h', 'إتصالات + فودافون'), ('i', 'إتصالات + أورنج')], max_length=30, null=True, verbose_name='نوع الشريحة')),
                ('paysystem', models.CharField(choices=[('a', 'كاش'), ('b', 'قسط'), ('c', 'قسط مريح'), ('d', 'تأمين')], max_length=30, null=True, verbose_name='نظام الدفع')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customersApp.sellers')),
            ],
        ),
    ]
