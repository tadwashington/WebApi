# -*- coding: utf-8 -*-
from scapy.all import *

# ICMPパケットの作成
request=IP(dst='www.yahoo.co.jp')/ICMP()
request.show()

# ICMPパケットの送出
response = sr1(request)

# 結果の表示
response.show()
