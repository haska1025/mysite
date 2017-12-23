from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    confid = models.IntegerField()
    uid = models.IntegerField()

class IOStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gid = models.IntegerField()
    recvbytes = models.IntegerField()
    sendbytes = models.IntegerField()
    recvpkgs = models.IntegerField()
    sendpkgs = models.IntegerField()
    clearpkgs = models.IntegerField()
    cachepkgs = models.IntegerField()
    clearbytes = models.IntegerField()
    cachebytes = models.IntegerField()
    recvlosts = models.IntegerField() 

