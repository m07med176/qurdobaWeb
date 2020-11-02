from django.shortcuts import render
from django.http import HttpResponse , FileResponse , JsonResponse
def showCustoemrs(request):
    return HttpResponse('welecom')