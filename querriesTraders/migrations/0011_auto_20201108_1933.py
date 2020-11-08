# Generated by Django 3.1.2 on 2020-11-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querriesTraders', '0010_auto_20201108_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querrysellers',
            name='nameOfMandoop',
            field=models.CharField(choices=[('فايز', 'وليد'), ('فايز', 'فايز'), ('حسن', 'حسن'), ('إبراهيم', 'إبراهيم'), ('خط دكرنس', 'خط دكرنس')], max_length=50, verbose_name='إسم المندوب'),
        ),
    ]