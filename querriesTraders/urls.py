from django.urls import path
from querriesTraders import views
from django.conf.urls import include, url
from django_file_download import views as file_views

urlpatterns = [
    path('form/', views.formQuerry,name='form'),
    path('table/', views.showTable,name='table'),
    path('extract/', views.extractExcelTable,name='extract'),
    path('datatable/', views.datatable,name='datatable'),
    url(r'^download$', file_views.file_download, name='file_download'),
    # path('download/', views.DownloadExcelTable,name='download'),
               ]