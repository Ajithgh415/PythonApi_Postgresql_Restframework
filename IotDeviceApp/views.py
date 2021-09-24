from typing import Any
from django.db.models.fields import CharField
from django.http import response, request
from django.http.request import HttpHeaders
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from IotDeviceApp.serializers import ParseSerializer
from django.core.files.storage import default_storage
from IotDeviceApp.models import Parse


# Create your views here.
@csrf_exempt
def ParseApi(request, id=0):
    if request.method == 'GET':
        datas = Parse.objects.all()
        data_serializer = ParseSerializer(datas, many=True)
        return_data = {}
        return_data['subID'] = data_serializer.data[0]['subID']
        return_data['tkn'] = data_serializer.data[0]['tkn']
        return_data['pri'] = data_serializer.data[0]['pri']
        return_data['dev'] = data_serializer.data[0]['dev']
        return_data['evt'] = data_serializer.data[0]['evt']
        return_data['time'] = data_serializer.data[0]['time']
        return_data['scnItms'] = [
        {
            'mac': data_serializer.data[0]['mac'],
            'thing': data_serializer.data[0]['thing'],
            'devName': data_serializer.data[0]['devName'],
            'aID': data_serializer.data[0]['aID'],
            'rID':data_serializer.data[0]['rID'],
            'rssi':data_serializer.data[0]['rssi'],
            'txP':data_serializer.data[0]['txP'],
            'bat':data_serializer.data[0]['bat'],
            'scnTime':data_serializer.data[0]['scnTime'],
            'scnCnt':data_serializer.data[0]['scnCnt'],
            'addData':
            {
                'mov':  data_serializer.data[0]['mov'],
                'temp':  data_serializer.data[0]['temp'],
                'hmd':data_serializer.data[0]['hmd'],
                'pres':data_serializer.data[0]['pres'],
                'io1':data_serializer.data[0]['io1'],
                'io2':data_serializer.data[0]['io2'],
                'Icn':data_serializer.data[0]['Icn'],
            }
            }
        ]
        return_data['msg'] = data_serializer.data[0]['msg']
            #return JsonResponse(data_serializer.data, safe=False)
        return JsonResponse(return_data, safe=False)

    elif request.method == 'POST':
        data_parse = JSONParser().parse(request)
        data_serializer = ParseSerializer(data=data_parse)
        print(data_serializer.is_valid())
        if data_serializer.is_valid():
           data_serializer.save()
           return JsonResponse({"status": "success", "data":data_serializer.data},safe=False)
        return JsonResponse({"status": "error", "data": data_serializer._errors}, safe=False)

    elif request.method=='PUT':
        data_parse=JSONParser().parse(request)
        datas=Parse.objects.get(subID=data_parse['subID'])
        data_serializer=ParseSerializer(datas,data=data_parse)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)

    elif request.method=='DELETE':
        datas=Parse.objects.get(aID=id)
        datas.delete()
        return JsonResponse("Deleted Successfully",safe=False)