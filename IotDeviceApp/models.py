from datetime import datetime
from re import T
from django.db import models

# Create your models here.
class Parse(models.Model):   
    subID = models.CharField(max_length=500)
    tkn = models.BigIntegerField()
    pri = models.CharField(max_length=500)
    dev = models.CharField(max_length=500)
    evt = models.CharField(max_length=500)
    time = models.DateTimeField(max_length=500)
    mac = models.CharField(max_length=500)
    thing = models.CharField(max_length=500)
    devName = models.CharField(max_length=500)
    aID = models.SmallIntegerField()
    rID = models.SmallIntegerField()
    rssi = models.SmallIntegerField()
    txP = models.SmallIntegerField()
    bat = models.SmallIntegerField()
    scnTime = models.DateTimeField(max_length=500,default=datetime.now)
    scnCnt = models.SmallIntegerField()
    mov = models.SmallIntegerField()
    temp = models.SmallIntegerField()
    hmd = models.SmallIntegerField()
    pres = models.BigIntegerField()
    io1 = models.SmallIntegerField()
    io2 = models.SmallIntegerField()
    Icn = models.CharField(max_length=500)
    msg = models.CharField(max_length=100) 