from django.urls import path,include
from . import views
from .views import CodeView
from rest_framework import routers

# like admin register 
router = routers.DefaultRouter()
router.register('data',CodeView)
#-----------------------------

urlpatterns = [
    path('api/', include(router.urls)),
    path('' , views.fawryCodes),
]