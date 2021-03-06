# Generated by Django 3.1.2 on 2021-02-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagerIssues', '0002_auto_20210208_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesofservices',
            name='kindOfService',
            field=models.CharField(choices=[('إتصالات وإنترنت', 'إتصالات وإنترنت'), ('مرافق عامة', 'مرافق عامة'), ('خدمات المرور', 'خدمات المرور'), ('معاملات مالية وبنوك', 'معاملات مالية وبنوك'), (' فورى باى', 'فورى باى'), ('خدمات التاجر', 'خدمات التاجر'), ('التبرعات', 'التبرعات'), ('إشتراكات وإعلانات', 'إشتراكات وإعلانات'), ('التعليم', 'التعليم'), ('التأمين', 'التأمين'), ('خدمات أخرى', 'خدمات أخرى'), ('الأكواد الخطأ', 'الأكواد الخطأ')], max_length=50, verbose_name='نوع الخدمة'),
        ),
    ]
