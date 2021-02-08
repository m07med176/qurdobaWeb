from django.shortcuts import render
from django.http import HttpResponse , FileResponse , JsonResponse

#--------------------------------------
from rest_framework import viewsets
from .serializers import CodeSerializer
from .models import CodesOfServices

class CodeView(viewsets.ModelViewSet):
    queryset = CodesOfServices.objects.all()
    serializer_class = CodeSerializer
#--------------------------------------

def fawryCodes(request):
    HttpResponse('welecom') 