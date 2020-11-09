from django import forms
from django.db import models
from django.core.validators import RegexValidator
from customersApp.models import Sellers
from django_google_maps import fields as map_fields
numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')



class QuerrySellers(models.Model):
        ## -------- بيانات التاجر -------------------
        nameOfMandoops = [("فايز", "وليد"),
                     ("فايز", "فايز"),
                     ("حسن", "حسن"),
                     ("إبراهيم", "إبراهيم"),
                     ("خط دكرنس", "خط دكرنس"),
                          ]
        nameOfMandoop = models.CharField(max_length=50,verbose_name = "إسم المندوب",choices =nameOfMandoops)
        areas = [("نبروه", "نبروه"),
                     ("بلقاس", "بلقاس")]
        area = models.CharField(max_length=50,verbose_name = "المنطقة",choices =areas)
        activityKinds = [("سنترال وخدمات محمول", "سنترال وخدمات محمول"),
                         ("خدمات كمبيوتر", "خدمات كمبيوتر"),
                         ("عطارة", "عطارة"),
                         ("مكتبة", "مكتبة"),
                         ("بقالة", "بقالة"),
                         ("سوبر ماركت", "سوبر ماركت"),
                         ("other", "أخر: ")
                         ]
        activityKind = models.CharField(max_length=20,choices=activityKinds,null=True,verbose_name = "نوع النشاط ")
        shopName = models.CharField(max_length=50,null=True,verbose_name = "إسم المحل ")
        ownerName = models.CharField(max_length=50,null=True,verbose_name = "إسم صاحب العمل ")
        phoneNumber = models.CharField(max_length=50,null=True,verbose_name = "رقم التليفون ",validators=[numeric])
        address = models.TextField(max_length=100,null=True,verbose_name = "العنوان بالتفصيل ")
        machinesOfepays=[("امان", "امان"),
                         ("فورى", "فورى"),
                         ("بى", "بى"),
                         ("مصارى", "مصارى"),
                         ("ضامن", "ضامن"),
                         ("سداد", "سداد")]
        machinesOfepay = models.CharField(max_length=20,choices=machinesOfepays,null=True,verbose_name = "مكن الدفع الإلكترونى ",editable=True)
        tayers = [("يوجد", "يوجد"),
                     ("لا يوجد", "لا يوجد") ]
        tayer = models.CharField(max_length=20,choices=tayers,null=True,verbose_name = "الطاير ")
        intention = models.CharField(max_length=100,null=True,verbose_name = "ما مدى قابليته للتعامل معنا")
        amountOfTreats=[
            ("اقل من 10 الاف", "اقل من 10 الاف"),
            ("من 10 الاف ل 25000", "من 10 الاف ل 25000"),
            ("من 25 الف ل 50 الف", "من 25 الف ل 50 الف"),
            ("اعلي من 50 الف", "اعلي من 50 الف")]
        amountOfTreat = models.CharField(max_length=20,choices=amountOfTreats,null=True,verbose_name = "حجم التعامل ")
        kindOfMobiles=[
            ("سامسونج", "سامسونج"),
            ("هواوى", "هواوى"),
            ("أبل", "أبل"),
            ("شاومى", "شاومى"),
            ("نوكيا", "نوكيا"),
            ("انفنكس", "انفنكس"),
            ("أوبو", "أوبو")]
        kindOfMobile = models.CharField(max_length=20,choices=kindOfMobiles,null=True,verbose_name = "نوع اجهزه المحمول")
        sims=[
            ("فودافون", " فودافون"),
            ("إتصالات", "إتصالات"),
            ("أورنج", "أورنج"),
                ]
        sim = models.CharField(max_length=20,choices=sims,null=True,verbose_name = "الكارت")
        evaluates=[
            ("مهم", "مهم"),
            ("مهم جدا", "مهم جدا"),
            ("متوسط", "متوسط"),
            ("غير مهم", "غير مهم"),
        ]
        evaluate = models.CharField(max_length=20,choices=evaluates,null=True,verbose_name = "التقييم")

        notes = models.TextField(max_length=100,null=True,verbose_name = "الملاحظات")
        date = models.DateField(null=True,verbose_name = "التاريخ")
        time = models.TimeField(null=True,verbose_name = "الوقت")

            # ----------------- google location ------------------#
        addressmap = map_fields.AddressField(max_length=200,null=True)
        geolocation = map_fields.GeoLocationField(max_length=100,null=True)

        def __str__(self):
            return self.ownerName
        
        # CharField
        # , widget=forms.RadioSelect()


class Devices(models.Model):
    deviceName = models.CharField(max_length=20, verbose_name="نوع الجهاز", null=True)
    kind = models.CharField(max_length=20, verbose_name="النوع", null=True)
    raterName = models.CharField(max_length=20, verbose_name="إسم المقيم", null=True)
    raterid = models.IntegerField(null=True,verbose_name="المقيم")
    rate = models.FloatField(verbose_name="التقييم", null=True)
    date = models.DateField(verbose_name="التاريخ", null=True)
    time = models.TimeField(verbose_name="الوقت", null=True)