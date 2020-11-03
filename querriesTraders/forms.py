from django import forms
from django.forms import Textarea
from django.core.validators import RegexValidator
from customersApp.models import Sellers
from querriesTraders.models import QuerrySellers,Devices
numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')
class QuerryFormSellers(
    forms.Form
    # ,forms.ModelForm
):
    ## -------- بيانات التاجر -------------------
    nameOfMandoops = [("وليد", "وليد"),
                      ("فايز", "فايز"),
                      ("حسن", "حسن"),
                      ("إبراهيم", "إبراهيم"), ]
    nameOfMandoop = forms.CharField(required=True,label="إسم المندوب",widget=forms.Select(choices=nameOfMandoops))
    areas = [("نبروه", "نبروه"),
             ("بلقاس", "بلقاس")]
    area = forms.CharField( required=True,label="المنطقة",widget=forms.Select(choices=areas))
    activityKinds = [("سنترال وخدمات محمول", "سنترال وخدمات محمول"),
                     ("خدمات كمبيوتر", "خدمات كمبيوتر"),
                     ("other", "أخر: "),
                     ]
    activityKind = forms.ChoiceField(widget=forms.RadioSelect(attrs={'id':"other-choice"}),choices=activityKinds, required=True,label="نوع النشاط ")

    shopName = forms.CharField(max_length=50, required=True,label="إسم المحل ")
    ownerName = forms.CharField(max_length=50, required=True,label="إسم صاحب العمل ")
    phoneNumber = forms.CharField(max_length=50, required=True,label="رقم التليفون ", validators=[numeric])
    address = forms.CharField(max_length=100,widget=forms.Textarea(attrs={'rows': 4, 'cols': 20,'style':"height: 77px;"}), required=True,label="العنوان بالتفصيل ")
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

    notes = forms.CharField(max_length=100,widget=forms.Textarea(attrs={'rows': 4, 'cols': 20,'style':"height: 77px;"}), required=False,label="الملاحظات")


    # ## this is for model form id dont know it yet
    # notes = {
    #         forms.CharField: {'widget': Textarea(
    #                            attrs={'rows': 1,
    #                                   'cols': 20,
    #                                   'style': 'height: 1em;'})},
    #     }
    # class Meta:
    # ## this is for model form id dont know it yet
    #     model = QuerrySellers
    #     exclude = ['id']  #?

class QuerryFormSellers2(forms.ModelForm):
    class Meta:
        model = QuerrySellers
        fields = '__all__'