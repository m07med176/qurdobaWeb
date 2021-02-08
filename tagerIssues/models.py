from django.db import models

class CodesOfServices(models.Model):
    nameOfService = models.CharField(max_length=50,verbose_name = "إسم الخدمة",null=True)
    codeOfService = models.IntegerField(verbose_name = "كود الخدمة",null=True)
    services = [("إتصالات وإنترنت", "إتصالات وإنترنت"),
                ("مرافق عامة", "مرافق عامة"),
                ("خدمات المرور", "خدمات المرور"),
                ("معاملات مالية وبنوك", "معاملات مالية وبنوك"),
                (" فورى باى", "فورى باى"),
                ("خدمات التاجر", "خدمات التاجر"),
                ("التبرعات", "التبرعات"),
                ("إشتراكات وإعلانات", "إشتراكات وإعلانات"),
                ("التعليم", "التعليم"),
                ("التأمين", "التأمين"),
                ("خدمات أخرى", "خدمات أخرى"),
                ("الأكواد الخطأ", "الأكواد الخطأ"),
                          ]
    kindOfService = models.CharField(max_length=50,verbose_name = "نوع الخدمة",choices=services)

    def __str__(self):
            return self.nameOfService