import os

import urllib

import json
from django.shortcuts import render
from django.http import HttpResponse , FileResponse , JsonResponse
from django.core.files.storage import FileSystemStorage
from pathlib import Path
from querriesTraders.forms import QuerryFormSellers,QuerryFormSellers2
from querriesTraders.models import QuerrySellers,Devices
from django.template.loader import render_to_string
import pandas as pd
from datetime import datetime
from wsgiref.util import FileWrapper

def enhaceData(lastData):
    data = str(lastData).replace('[', '').replace(']', '').replace(',', '-').replace("'", '')
    return data
def handelEpays(lastData):
    while '' in lastData: lastData.remove('')
    data = str(lastData).replace('[', '').replace(']', '').replace(',', '-').replace("'", '')
    unhandelled_data = data.replace(' -', "").strip('-').split('-')
    data = []
    for n,i  in enumerate(unhandelled_data):
        count = len(unhandelled_data)
        key = i.strip()
        if count-n == 1:
            value = unhandelled_data[unhandelled_data.index(i)].strip()
        else:
            value = unhandelled_data[unhandelled_data.index(i)+1].strip()
        lvalue = unhandelled_data[unhandelled_data.index(i)-1].strip()
        if key in ['فورى', 'امان','بى','مصارى']:
            if value not in ['فورى', 'امان','بى','مصارى']:
                data.append(key+"("+value+")")
            else:
                data.append(key)
        else:
            if lvalue not in ['فورى', 'امان', 'بى', 'مصارى']:
                data.append(key)

    data = str(data).replace('[', '').replace(']', '').replace(',', '-').replace("'", '')
    return data
def formQuerry(request):
    # if request.is_ajax and request.method == "POST":
    #     acaaa = request.POST.get('data', None)
    #     print(acaaa)
    for i in request.POST:
        print(i,request.POST[i])
    dataRespose = {}
    dataRespose['message'] = "عفوا حدث خطأ أثناء التسجيل"
    dataRespose['status'] = "false"
    if request.method == 'POST':
        nameOfMandoop = request.POST.get('nameOfMandoop')
        area = request.POST.get('area').strip()
        activityKind = request.POST.getlist('activityKind')

        if activityKind[1] != '':
            activityKind = activityKind[1].strip()
        else:
            activityKind = activityKind[0]

        shopName = request.POST.get('shopName').strip()
        ownerName = request.POST.get('ownerName').strip()
        phoneNumber = request.POST.get('phoneNumber').strip()
        address = request.POST.get('address').strip()

        machinesOfepay = request.POST.getlist('machinesOfepay')
        if 'other' in machinesOfepay:machinesOfepay.remove('other')
        machinesOfepayForQuerry = handelEpays(machinesOfepay)

        tayer = request.POST.get('tayer')
        intention = request.POST.get('intention').strip()
        amountOfTreat = request.POST.get('amountOfTreat')

        kindOfMobile = request.POST.getlist('kindOfMobile')
        dataCollector = {}
        dataOfRating = {}
        dataOfRatingl = []
        for i in kindOfMobile:
            if i.replace('.','',1).isdigit() and float(i) > 0:
                dataOfRating[kindOfMobile[kindOfMobile.index(i)-1]]=float(i)
                dataOfRatingl.append(kindOfMobile[kindOfMobile.index(i)-1]+"("+i+")")
        mabalashellondamana= request.POST.get('kindOfMobilebalash').strip()

        kindOfMobileForQuerry= enhaceData(dataOfRatingl)+"-"+mabalashellondamana
        sim = request.POST.getlist('sim')
        dataOfRatingSim = {}
        dataOfRatingSiml = []
        for i in sim:
            if i.replace('.', '', 1).isdigit() and float(i) > 0:
                dataOfRatingSim[sim[sim.index(i) - 1]] = float(i)
                dataOfRatingSiml.append(sim[sim.index(i) - 1] + "(" + i + ")")
        cardnotes = request.POST.get('cardnotes').strip()
        simQuerry = enhaceData(dataOfRatingSiml)+"-"+cardnotes
        dataCollector['mobile']=dataOfRating
        dataCollector['sim']=dataOfRatingSim
        evaluate = request.POST.get('evaluate').strip()
        notes = request.POST.get('notes').strip()
        dateOfquerry = str(datetime.now().date())
        timeOfquerry = str(datetime.now().time()).split('.')[0]
        data = QuerrySellers(nameOfMandoop=nameOfMandoop,
                  area=area,
                  activityKind=activityKind,
                  shopName=shopName,
                  ownerName=ownerName,
                  phoneNumber=phoneNumber,
                  address=address,
                  machinesOfepay=machinesOfepayForQuerry,
                  sim=simQuerry,
                  tayer=tayer,
                  intention=intention,
                  amountOfTreat=amountOfTreat,
                  kindOfMobile=kindOfMobileForQuerry,
                  evaluate=evaluate,
                  notes=notes,
                  date=dateOfquerry,
                  time=timeOfquerry,
                  )
        data.save()
        # ---------------- insert in database of device ----------------- #
        # dataOfRating.update(dataOfRatingSim)
        raterid=QuerrySellers.objects.latest('id').id
        for data in dataCollector:
            for item in dataCollector[data]:
                devicesRate = Devices(
                    kind=data,
                    deviceName= item,
                    raterName = ownerName,
                    raterid = raterid,
                    rate= dataCollector[data][item],
                    date=dateOfquerry,
                    time=timeOfquerry,
                    )
                devicesRate.save()
        dataRespose['message'] = "تم التسجيل بنجاح"
        dataRespose['status'] = "true"
        return HttpResponse(
            json.dumps(dataRespose),
            content_type="application/json"
        )
        #return JsonResponse(dataRespose)

    return render(request,'querriesTraders/form.html',{'form':QuerryFormSellers})

def showTable(request):
    all_data = QuerrySellers.objects.all()
    return render(request,'querriesTraders/details.html',{'all_data':all_data})

def datatable(request):
    all_data = QuerrySellers.objects.all()
    return render(request,'querriesTraders/datatable.html',{'all_data':all_data})

def extractExcelTable(request):
    BASE_DIR = Path(__file__).resolve().parent.parent

    all_data = QuerrySellers.objects.all()
    content = render_to_string('querriesTraders/datatable.html', {'all_data':all_data})
    for i, df in enumerate(pd.read_html(content)):
        df.to_excel(f'querriesTraders/data/excelOfSellers_{i}.xls')
        filename = BASE_DIR / f'querriesTraders/data/excelOfSellers_{i}.xls'
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
            machinesOfepay = theForm.cleaned_data.getlist('machinesOfepay')
            tayer = theForm.cleaned_data.get('tayer')
            intention = theForm.cleaned_data.get('intention')
            amountOfTreat = theForm.cleaned_data.get('amountOfTreat')
            kindOfMobile = theForm.cleaned_data.getlist('kindOfMobile')
            evaluate = theForm.cleaned_data.get('evaluate')
            notes = theForm.cleaned_data.get('notes')
            data = QuerrySellers(nameOfMandoop=nameOfMandoop,
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