import pyperclip
import pyautogui
from http import client
from hashlib import md5
import urllib.parse
import random
import json
pyautogui.hotkey('ctrl', 'c')
sentence = pyperclip.paste()
if sentence[0] >= u'\u4e00' and sentence[0] <= u'\u9fa5':
    fromLang = 'auto'
    toLang = 'en'
else:
    fromLang = 'auto'
    toLang = 'zh'
# enter your appid
appid = ''
# enter your secretkey
secretKey = '' 
myurl = '/api/trans/vip/translate'
salt = random.randint(32768, 65536)
sentence = sentence.replace('\n', ' ')
sign = appid + sentence + str(salt) + secretKey
m1 = md5(sign.encode(encoding='utf-8'))
sign = m1.hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(sentence) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
try:
    httpClient = client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
    response = httpClient.getresponse()
    result = response.read()
    result = json.loads(result)['trans_result'][0]['dst']
except:
    result = '未联网'
finally:
    if httpClient:
        httpClient.close()
try:
    # pyperclip.copy('api.fanyi.baidu.com/' + myurl)
    pyperclip.copy(result)
    pyautogui.alert(result, title='翻译结果')
except:
    pass
