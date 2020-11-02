from django import forms
from django.db import models
from django.core.validators import RegexValidator
from customersApp.models import Sellers
numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')
class QuerrySellers(models.Model):
        ## -------- بيانات التاجر -------------------
        nameOfMandoops = [("a", "وليد"),
                     ("b", "فايز"),
                     ("c", "حسن"),
                     ("d", "إبراهيم"),]
        nameOfMandoop = models.CharField(max_length=50,verbose_name = "إسم المندوب",choices =nameOfMandoops)
        areas = [("a", "نبروه"),
                     ("b", "بلقاس")]
        area = models.CharField(max_length=50,verbose_name = "المنطقة",choices =areas)
        activityKinds=[("a", "سنترال وخدمات محمول"),
                     ("b", "خدمات كمبيوتر")]
        activityKind = models.CharField(max_length=20,choices=activityKinds,verbose_name = "نوع النشاط ",editable=True)
        shopName = models.CharField(max_length=50,verbose_name = "إسم المحل ")
        ownerName = models.CharField(max_length=50,verbose_name = "إسم صاحب العمل ")
        phoneNumber = models.CharField(max_length=50,verbose_name = "رقم التليفون ",validators=[numeric])
        address = models.TextField(max_length=100,verbose_name = "العنوان بالتفصيل ")
        machinesOfepays = [("a", "امان"),
                     ("b", "فورى"),
                     ("c", "بى"),
                     ("d", "مصارى"),
                     ("e", "ضامن"),
                     ("f", "سداد"),
                           ]
        machinesOfepay = models.CharField(max_length=20,choices=machinesOfepays,verbose_name = "مكن الدفع الإلكترونى ",editable=True)
        tayers = [("a", "يوجد"),
                     ("b", "لا يوجد") ]
        tayer = models.CharField(max_length=20,choices=tayers,verbose_name = "الطاير ")
        intention = models.CharField(max_length=100,null=True,verbose_name = "ما مدى قابليته للتعامل معنا")
        amountOfTreats=[
            ("a", "اقل من 10 الاف"),
            ("b", "من 10 الاف ل 25000"),
            ("c", "من 25 الف ل 50 الف"),
            ("d", "اعلي من 50 الف")]
        amountOfTreat = models.CharField(max_length=20,choices=amountOfTreats,verbose_name = "حجم التعامل ")
        kindOfMobiles=[
            ("a", "سامسونج"),
            ("b", "هواوى"),
            ("c", "أبل"),
            ("d", "شاومى"),
            ("e", "نوكيا"),
            ("f", "انفنكس"),
            ("g", "أوبو")]
        kindOfMobile = models.CharField(max_length=20,choices=kindOfMobiles,verbose_name = "نوع اجهزه المحمول")
        evaluates=[
            ("a", "مهم"),
            ("b", "مهم جدا"),
            ("c", "متوسط"),
            ("d", "غير مهم"),
        ]
        evaluate = models.CharField(max_length=20,choices=evaluates,verbose_name = "التقييم")

        notes = models.TextField(max_length=100,verbose_name = "الملاحظات")
        
        # CharField
        # , widget=forms.RadioSelect()