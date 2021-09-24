from django.db.models import fields
from rest_framework import serializers
from IotDeviceApp.models import Parse

class ParseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Parse
        fields=(
            'subID',
            'tkn',
            'pri',
            'dev',
            'evt',
            'time',
            'mac',
            'thing',
            'devName',
            'aID',
            'rID',
            'rssi',
            'txP',
            'bat',
            'scnTime',
            'scnCnt',
            'mov',
            'temp',
            'hmd',
            'pres',
            'io1',
            'io2',
            'Icn',
            'msg'
            )
        