#-*coding:utf8
from django.db import models
from django.contrib.auth.models import User

class ProUser(models.Model):
    user = models.OneToOneField(User)
    tel = models.CharField(max_length=20,verbose_name=u'联系方式')
    addr = models.CharField(max_length=50,verbose_name=u'派送地址')
    QQ  = models.CharField(max_length=15,null=True,blank=True,verbose_name=u'QQ')

class Goods(models.Model):
    name       = models.CharField(max_length=20)
    price      = models.FloatField() 
    img        = models.FileField(upload_to="./goodsImg/") 
    category   = models.ForeignKey("Category") 
    def __unicode__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    p_category    = models.ForeignKey("self",null=True,blank=True)
    def __unicode__(self):
        return self.category_name

class LineItem(models.Model):  
    goods       = models.ForeignKey(Goods)  
    goods_price = models.FloatField()  
    quantity    = models.IntegerField() 
    def __unicode__(self):
        return self.goods 





'''
class ShopCar(models.Model):
    user = models.OneToOneField(User)
    goods = models.ManyToManyField(Goods)
    def __unicode__(self):
        return self.user
    
    def add_goods(self):
        pass

    def remove_goods(self):
        pass

    def update_goods(self):
        pass

'''











