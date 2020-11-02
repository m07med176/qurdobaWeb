from django.db import models

# Create your models here.
class Sellers(models.Model):
    sellerName = models.CharField(max_length=50,verbose_name = "إسم المندوب")
    region = models.CharField(max_length=20,null=True,verbose_name = "المنطقة")
    phoneno = models.IntegerField(null=True,verbose_name = "رقم التليفون")

    def __str__(self):
        return self.sellerName

class Customers(models.Model):
    # ------------------ بيانات العميل --------------------
    name = models.CharField(max_length =50,null=False,verbose_name = "الإسم")
    kindshops = [("a","بقالة"),
                 ("b","منظفات"),
                 ("c","سنترال"),
                 ("d","صيانة محمول"),
                 ("e","إكسسوارات محمول"),
                 ("f","أدوات صحية"),
                 ("g","مكتبة"),
                 ("h","خردوات"),
                 ("y","شخصى")]
    kindshop = models.CharField(max_length=30, null=True, verbose_name ="نوع المحل",choices=kindshops)
    nameshop = models.CharField(max_length=30, null=True, verbose_name ="إسم المحل")
    phoneno = models.IntegerField(null=True,verbose_name = "رقم التليفون")
    idno = models.IntegerField(null=True,verbose_name = "الرقم القومى")
    address = models.TextField(max_length =100,null=True,verbose_name = "العنوان")
    date = models.DateField(max_length =11,null=True,verbose_name = "تاريخ التسجيل")
    # ------------------- photos ---------------------------
    cardImageFront = models.ImageField(upload_to="UserImages/cards",null=True,verbose_name = "صورة البطاقة وجه")
    cardImageBack = models.ImageField(upload_to="UserImages/cards",null=True,verbose_name = "صورة البطاقة ظهر")
    proofImage = models.ImageField(upload_to="UserImages/attached",null=True,verbose_name = "صور وصل")
    # --------------------- بيانات الخدمة -------------------
    servicekinds = [("a","ماكينة"),
                    ("b","تطبيق")]
    servicekind = models.CharField(max_length=30,null=True,verbose_name = "نوع الخدمة",choices=servicekinds)
    accountNo = models.IntegerField(null=True,verbose_name = "رقم الحساب")
    deviceserial = models.CharField(max_length =50,null=True,verbose_name = "سيريال الجهاز")
    servicestates = [("a",'مفعلة'),
                     ("b",'غير مفعلة'),
                     ("c",'موقوفة')]
    servicestate = models.CharField(max_length=30,null=True,verbose_name = "حاله الخدمة",choices=servicestates)
    # -------------- machine case ---------------------------
    kindmachines=[("a","520 C زيرو"),
                  ("b","520 C كسر"),
                  ("c","520 Contact زيرو"),
                  ("d","520 Contact كسر"),
                  ("e","520 Contact زيرو بدون بطارية"),
                  ("f","520 Contact كسر بدون بطارية")]
    kindmachine = models.CharField(max_length=30,null=True,verbose_name = "نوع الجهاز",choices=kindmachines)
    kindphones = [("a","فودافون"),
                  ("b","اورنج"),
                  ("c","إتصالات"),
                  ("d","فودافون + أورنج"),
                  ("e","فودافون + إتصالات"),
                  ("f","أورنج + فودافون"),
                  ("g","أورنج + إتصالات"),
                  ("h","إتصالات + فودافون"),
                  ("i","إتصالات + أورنج")]
    kindphone = models.CharField(max_length=30,null=True,verbose_name = "نوع الشريحة",choices=kindphones)
    paysystems = [("a","كاش"),
                  ("b","قسط"),
                  ("c","قسط مريح"),
                  ("d","تأمين")]
    paysystem = models.CharField(max_length=30,null=True,verbose_name = "نظام الدفع",choices=paysystems)
    # relation
    seller = models.ForeignKey(Sellers,on_delete = models.PROTECT)

    def __str__(self):
        return self.name
