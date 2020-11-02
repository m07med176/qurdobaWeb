from django import forms
from django.core.validators import RegexValidator
from customersApp.models import Sellers
from querriesTraders.models import QuerrySellers
numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')
class QuerryFormSellers(forms.Form):
    ## -------- بيانات التاجر -------------------
    nameOfMandoops = [("وليد", "وليد"),
                      ("فايز", "فايز"),
                      ("حسن", "حسن"),
                      ("إبراهيم", "إبراهيم"), ]
    nameOfMandoop = forms.ChoiceField(required=True,label="إسم المندوب",widget=forms.RadioSelect(),choices=nameOfMandoops)
    areas = [("نبروه", "نبروه"),
             ("بلقاس", "بلقاس")]
    area = forms.CharField( required=True,label="المنطقة",widget=forms.Select(choices=areas))
    activityKinds = [("سنترال وخدمات محمول", "سنترال وخدمات محمول"),
                     ("خدمات كمبيوتر", "خدمات كمبيوتر")]
    activityKind = forms.ChoiceField(widget=forms.RadioSelect(),choices=activityKinds, required=True,label="نوع النشاط ")

    shopName = forms.CharField(max_length=50, required=True,label="إسم المحل ")
    ownerName = forms.CharField(max_length=50, required=True,label="إسم صاحب العمل ")
    phoneNumber = forms.CharField(max_length=50, required=True,label="رقم التليفون ", validators=[numeric])
    address = forms.CharField(max_length=100,widget=forms.Textarea, required=True,label="العنوان بالتفصيل ")
    machinesOfepays = [("امان", "امان"),
                       ("فورى", "فورى"),
                       ("بى", "بى"),
                       ("مصارى", "مصارى"),
                       ("ضامن", "ضامن"),
                       ("سداد", "سداد"),
                       ]
    machinesOfepay = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=machinesOfepays, required=True,label="مكن الدفع الإلكترونى ")
    tayers = [("يوجد", "يوجد"),
              ("لا يوجد", "لا يوجد")]
    tayer = forms.ChoiceField(widget=forms.RadioSelect(),choices=tayers, required=True,label="الطاير ")
    intention = forms.CharField(max_length=100,label="",required=False,widget=forms.TextInput(attrs={'placeholder': "ما مدى قابليته للتعامل معنا ?"}))

    amountOfTreats = [
        ("اقل من 10 الاف", "اقل من 10 الاف"),
        ("من 10 الاف ل 25000", "من 10 الاف ل 25000"),
        ("من 25 الف ل 50 الف", "من 25 الف ل 50 الف"),
        ("اعلي من 50 الف", "اعلي من 50 الف")]
    amountOfTreat = forms.ChoiceField(widget=forms.RadioSelect(),choices=amountOfTreats, required=True,label="حجم التعامل ")
    kindOfMobiles = [
        ("سامسونج", "سامسونج"),
        ("هواوى", "هواوى"),
        ("أبل", "أبل"),
        ("شاومى", "شاومى"),
        ("نوكيا", "نوكيا"),
        ("انفنكس", "انفنكس"),
        ("أوبو", "أوبو")]
    kindOfMobile = forms.MultipleChoiceField( widget=forms.CheckboxSelectMultiple,choices=kindOfMobiles, required=True,label="نوع اجهزه المحمول")
    evaluates = [
        ("مهم", "مهم"),
        ("مهم جدا", "مهم جدا"),
        ("متوسط", "متوسط"),
        ("غير مهم", "غير مهم"),
    ]
    evaluate = forms.ChoiceField(widget=forms.RadioSelect(),choices=evaluates, required=True,label="التقييم")

    notes = forms.CharField(max_length=100,widget=forms.Textarea, required=False,label="الملاحظات")


class QuerryFormSellers2(forms.ModelForm):
    class Meta:
        model = QuerrySellers
        fields = '__all__'