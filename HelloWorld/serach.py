# -*- coding: utf-8 -*-
import usaddress
from django.http import HttpResponse
from django.shortcuts import render


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def search_form(request):
    return render(request, 'search_form.html')
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        addr = request.GET['q']
        json_addr = usaddress.parse(addr)

        text = '城市:' + (json_addr[5][0]) + '地址:' + (json_addr[2][0]) + ' ' + (json_addr[3][0]) + ' ' + (
            json_addr[4][0]) + ' 邮编:' + (json_addr[7][0]) + ' 号码:' + (json_addr[8][0]) + (json_addr[9][0]) + (
                   json_addr[10][0])
        message = '内容为: ' + text
    else:
        message = '你提交了空表单'
    return HttpResponse(message)