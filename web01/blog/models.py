#-*coding:utf8
from django.db import models
from django.contrib.auth.models import User

class ProUser(models.Model):
    user = models.OneToOneField(User)
    tel = models.CharField(max_length=20,verbose_name=u'联系方式')
    addr = models.CharField(max_length=50,verbose_name=u'派送地址')
    QQ  = models.CharField(max_length=15,null=True,blank=True,verbose_name=u'QQ')

class GoodsType(models.Model):
    type_name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.type_name

class TeaType(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Tea(models.Model):
    name      = models.CharField(max_length=20)
    price     = models.FloatField() 
    img       = models.FileField(upload_to="./goodsImg/") 
    goodstype = models.ForeignKey(GoodsType) 
    teatype   = models.ForeignKey(TeaType) 
    def __unicode__(self):
        return self.name

class CakeType(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class TeaCake(models.Model):
    name      = models.CharField(max_length=20)
    price     = models.FloatField() 
    img       = models.FileField(upload_to="./goodsImg/") 
    goodstype = models.ForeignKey(GoodsType) 
    caketype  = models.ForeignKey(CakeType) 
    def __unicode__(self):
        return self.name

