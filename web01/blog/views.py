#-*coding:utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from blog.models import ProUser,Goods,Category
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect

class RegistUserForm(forms.ModelForm):
    username = forms.CharField(label=u'用户名')
    password = forms.CharField(label=u'口令',widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password') 

class RegistProUserForm(forms.ModelForm):
    class Meta:
        model = ProUser
        fields = ('tel','addr','QQ')

def index(req):
    goods_list    = Goods.objects.all()
    category_list = Category.objects.all() 
    categorys     = [category for category in category_list if category.p_category is None]
    if req.user.is_authenticated():
        return render(req,"index.html",{'user':req.user,'goods_list':goods_list,'categorys':categorys})
    else:
        return render(req,"index.html",{'goods_list':goods_list})

def regist_user(req):
    if req.method == "POST":
        rf1 = RegistUserForm(req.POST)
        rf2 = RegistProUserForm(req.POST)
        if rf1.is_valid() and rf2.is_valid():
            rf1.instance.is_staff = True
            rf1.instance.set_password(rf1.cleaned_data['password'])
            rf1.save()
            rf2.instance.user = rf1.instance 
            rf2.save()
            return HttpResponse("<h2>亲,你已经注册成功了哦!<br />到首页<b>登寻</b>找宝贝去吧~~</h2>")
    else:
        rf1 = RegistUserForm()
        rf2 = RegistProUserForm()
    return render(req,'regist.html',{'rf1':rf1,'rf2':rf2})
    
def login_user(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    user = authenticate(username=username,password=password)
    if user is not None:
        #print user.username 
        login(req,user)
        return HttpResponse(username)
    else:
        return HttpResponseRedirect('/index/')
'''
def disp_tea(req):
    goodstype    = GoodsType.objects.all()
    teatype      = TeaType.objects.all()
    caketype     = CakeType.objects.all()
    tid = req.GET.get('tid')
    tea_type = TeaType.objects.get(id=tid)
    tea_list = tea_type.tea_set.all()
    return render(req, 'disp_tea.html',{'tea_list':tea_list,'goodstype':goodstype,'teatype':teatype,'caketype':caketype})


def disp_cake(req):
    goodstype    = GoodsType.objects.all()
    teatype      = TeaType.objects.all()
    caketype     = CakeType.objects.all()
    cid = req.GET.get('cid')
    cake_type = CakeType.objects.get(id=cid)
    teacake_list = cake_type.teacake_set.all()
    return render(req, 'disp_cake.html',{'teacake_list':teacake_list,'goodstype':goodstype,'teatype':teatype,'caketype':caketype})



def logout_user(req):
    pass
def order(req):
    return render_to_response("order.html",{})
def pay(req):
    return render_to_response("pay.html",{})
    '''
