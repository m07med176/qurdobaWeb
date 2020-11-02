from django.urls import path
from querriesTraders import views

urlpatterns = [
    path('form/', views.formQuerry,name='form'),
    path('table/', views.showTable,name='table'),
    path('extract/', views.extractExcelTable,name='extract'),
    # path('download/', views.DownloadExcelTable,name='download'),
               ]