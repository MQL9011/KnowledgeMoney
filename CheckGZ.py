'''
    Create by MccRee
'''

import requests
import json

header = {
'POST':'/vote/add-1077304 HTTP/1.1',
'Host':'vzan.cc',
'Accept':'application/json, text/javascript, */*; q=0.01',
'X-Requested-With':	'XMLHttpRequest',
'Accept-Language':'zh-cn',
'Accept-Encoding':'br, gzip, deflate',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Origin':'https://vzan.cc',
'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 MicroMessenger/6.7.3(0x16070317) NetType/WIFI Language/zh_CN',
'Cookie':'Hm_lpvt_5c88f64ce16c5100a4a8509273257ce4=1542288926; Hm_lvt_5c88f64ce16c5100a4a8509273257ce4=1542245740; is_show_guanzhu_1077304=1; vzan_base_userinfo=BCD044F400833A156E045DA1F2DA86A9; vzanuserinfo1077304=4C2F249DF9BBA000292C7066645ADD1E',
}

param = {'pid':'49296',
         'vid':'16528',
        }
r = requests.post(url='https://vzan.cc/vote/add-1077304', data=json.dumps(param))

# r = requests.get('https://vzan.cc/vote/vdetail-1077304?vuid=49296&from=singlemessage&isappinstalled=0', headers=header)

print(r)