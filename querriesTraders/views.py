import os

import urllib
from django.shortcuts import render
from django.http import HttpResponse , FileResponse , JsonResponse
from django.core.files.storage import FileSystemStorage
from pathlib import Path
from querriesTraders.forms import QuerryFormSellers,QuerryFormSellers2
from querriesTraders.models import QuerrySellers as db
from django.template.loader import render_to_string
import pandas as pd
from wsgiref.util import FileWrapper
def formQuerry(request):
    if request.method == 'POST':
        nameOfMandoop = request.POST.get('nameOfMandoop')
        area = request.POST.get('area')
        activityKind = request.POST.get('activityKind')
        shopName = request.POST.get('shopName')
        ownerName = request.POST.get('ownerName')
        phoneNumber = request.POST.get('phoneNumber')
        address = request.POST.get('address')
        machinesOfepay = request.POST.get('machinesOfepay')
        tayer = request.POST.get('tayer')
        intention = request.POST.get('intention')
        amountOfTreat = request.POST.get('amountOfTreat')
        kindOfMobile = request.POST.get('kindOfMobile')
        evaluate = request.POST.get('evaluate')
        notes = request.POST.get('notes')
        data = db(nameOfMandoop=nameOfMandoop,
                  area=area,
                  activityKind=activityKind,
                  shopName=shopName,
                  ownerName=ownerName,
                  phoneNumber=phoneNumber,
                  address=address,
                  machinesOfepay=machinesOfepay,
                  tayer=tayer,
                  intention=intention,
                  amountOfTreat=amountOfTreat,
                  kindOfMobile=kindOfMobile,
                  evaluate=evaluate,
                  notes=notes
                  )
        data.save()
    return render(request,'querriesTraders/form.html',{'form':QuerryFormSellers})

def showTable(request):
    all_data = db.objects.all()
    return render(request,'querriesTraders/details.html',{'all_data':all_data})

def extractExcelTable(request):
    BASE_DIR = Path(__file__).resolve().parent.parent

    all_data = db.objects.all()
    content = render_to_string('querriesTraders/details.html', {'all_data':all_data})
    for i, df in enumerate(pd.read_html(content)):
        df.to_csv(f'data/excelOfSellers_{i}.csv')
        filename = BASE_DIR / f'data/excelOfSellers_{i}.csv'
        return render(request,'querriesTraders/download.html',{'filename':filename})





# def DownloadExcelTable(request):
#     BASE_DIR = Path(__file__).resolve().parent.parent
#     fs = FileSystemStorage(BASE_DIR/'data')
#     # response = HttpResponse(mimetype='application/force-download')  # mimetype is replaced by content_type for django 1.7
#     # FileResponse(fs.open('excelOfSellers_0.csv', 'rb'), content_type='application/force-download')
#     # response['Content-Disposition'] = 'attachment; filename="excelOfSellers_0.csv"'
#     # return response
#
#
#     filename = BASE_DIR/'data/excelOfSellers_0.csv'
#     wrapper = FileWrapper(filename)
#     response = HttpResponse(wrapper, content_type='text/plain')
#     response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
#     response['Content-Length'] = os.path.getsize(filename)
#     return response

def getFormQuerry(request):
    if request.method == 'POST':
        theForm =QuerryFormSellers(request.POST)
        if theForm.is_vaild():
            nameOfMandoop = theForm.cleaned_data.get('nameOfMandoop')
            area = theForm.cleaned_data.get('area')
            activityKind = theForm.cleaned_data.get('activityKind')
            shopName = theForm.cleaned_data.get('shopName')
            ownerName = theForm.cleaned_data.get('ownerName')
            phoneNumber = theForm.cleaned_data.get('phoneNumber')
            address = theForm.cleaned_data.get('address')
            machinesOfepay = theForm.cleaned_data.get('machinesOfepay')
            tayer = theForm.cleaned_data.get('tayer')
            intention = theForm.cleaned_data.get('intention')
            amountOfTreat = theForm.cleaned_data.get('amountOfTreat')
            kindOfMobile = theForm.cleaned_data.get('kindOfMobile')
            evaluate = theForm.cleaned_data.get('evaluate')
            notes = theForm.cleaned_data.get('notes')
            data = db(nameOfMandoop=nameOfMandoop,
                      area=area,
                      activityKind=activityKind,
                      shopName= shopName,
                      ownerName = ownerName,
                      phoneNumber = phoneNumber,
                      address = address,
                      machinesOfepay=machinesOfepay,
                      tayer=tayer,
                      intention=intention,
                      amountOfTreat=amountOfTreat,
                      kindOfMobile=kindOfMobile,
                      evaluate=evaluate,
                      notes=notes
                      )
            data.save()


    return HttpResponse('welecom')