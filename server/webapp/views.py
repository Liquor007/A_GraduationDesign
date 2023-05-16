from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.core.cache import cache  # 存入redis
import random
from django.core.mail import send_mail


from webapp.models import Users
from server import settings

from webapp.serializers import UsersSerializer
from rest_framework.decorators import api_view

# 生成随机字符串
def generate_random_str(randomlength=6):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

# Create your views here.
@api_view(['POST'])
def users_login(request):
    if request.method == 'POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            anyone=Users.objects.get(email=email,password=password)
        except Users.DoesNotExist:
            udata={
                "email":email,
                "password":"",
                "uid":""
            }
            return JsonResponse(udata, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        udata = {
            "email":anyone.email,
            "uid":anyone.uid
        }
        return JsonResponse(udata, status=status.HTTP_200_OK) 
@api_view(['POST'])
def users_captcha(request):
    if request.method == 'POST':
        email=request.POST.get("email")
        udata={
            "email":email,
            "password":"",
            "uid":""
        }
        try:
            anyone=Users.objects.get(email=email)
        except Users.DoesNotExist:#如果不存在该email
            code=generate_random_str()
            udata['captcha']=code#返回信息用于接口测试
            key='captcha_'+email
            # 发送验证码
            my_email = send_mail('激活验证', "验证码如下：\n"+code+"\n请在5分钟内完成注册", settings.DEFAULT_FROM_EMAIL, [email])
            cache.set(key, code, 30)  # 5分钟的有效时间
            return JsonResponse(udata, status=status.HTTP_200_OK)
        if anyone:#该邮箱已注册
            return JsonResponse(udata, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def users_register(request):
    if request.method == 'POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        captcha=request.POST.get("captcha")
        code = cache.get('captcha_'+email)
        udata={
            "email":email,
            "uid":""
        }
        if not code:# 验证码失效
            return JsonResponse(udata, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if code==captcha:# 注册成功
            newuser=Users(email=email,password=password)
            newuser.save()
            anyone=Users.objects.get(email=email)
            udata["uid"]=anyone.uid
            return JsonResponse(udata,status=status.HTTP_200_OK)
