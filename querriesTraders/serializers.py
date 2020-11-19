from .models import QuerrySellers,Devices
from rest_framework import serializers

# Serializers define the API representation.
class SellerDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ['User', 'fields','kind', 'raterName','raterid','rate']

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuerrySellers
        fields = ['nameOfMandoop',
                  'area',
                  'activityKind',
                  'shopName',
                  'ownerName',
                  'phoneNumber',
                  'address',
                  'machinesOfepay',
                  'sim',
                  'tayer',
                  'intention',
                  'amountOfTreat',
                  'kindOfMobile',
                  'evaluate',
                  'notes',
                  'date',
                  'time']
