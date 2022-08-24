# -*- coding: utf-8 -*-
from django.http import HttpResponse
import usaddress

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def hello(request):

    addr = 'Amy Clawson 1415 Marzelle ct. Joplin, MO 64801 417 529 2927'
    json_addr = usaddress.parse(addr)

    text ='城市:' + (json_addr[5][0]) + '地址:' + (json_addr[2][0]) + ' ' + (json_addr[3][0]) + ' ' + (
            json_addr[4][0]) + ' 邮编:' + (json_addr[7][0]) + ' 号码:' + (json_addr[8][0]) + (json_addr[9][0]) + (
          json_addr[10][0])
    return HttpResponse(text)

