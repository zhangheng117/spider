#coding:utf-8
#versions:python Anaconda3


import requests
import re
import json
from lxml import etree


s = requests.session()
headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }

url = 'https://accounts.douban.com/login'
html = s.get(url,headers=headers).text
captcha = etree.HTML(html).xpath('//*[@id="captcha_image"]/@src')
if len(captcha)>0:
    print('有验证码')

    captcha_id=etree.HTML(html).xpath('//div[@class="captcha_block"]//input[@name="captcha-id"]/@value')
    print(captcha_id[0])
    capach=s.get(captcha[0],headers=headers)
    with open('douban.jpg','wb') as f:
        f.write(capach.content)
        f.close()
    from PIL import Image
    try:
        img = Image.open('douban.jpg')
        img.show()
        img.close()
    except:
        pass
    yzm = input('请输入验证码\n>:')
    data={
        'source':'index_nav',
        'captcha-solution':yzm,
        'captcha-id':captcha_id[0],
        'redir':'https://www.douban.com/',
        'form_email':账号,
        'form_password':密码,
        'login':'登录'
    }
    html = s.post(url,data=data,headers=headers)
    if'小澎湃' in html.text:
        print('登录成功啦')
        print(html.url)
    else:
        print('失败')
else:
    post_data = {
                'form_email':账号,
                'form_password':密码,
                # 'redir':'https://www.douban.com/people/151968962/'
            }
    html = s.post('https://accounts.douban.com/login', data=post_data, headers=headers)

    if html.status_code==200:
        name = etree.HTML(html.text).xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]/text()')[0]
        if len(name)>1 and name==账号名称:
            print('登录成功啦')
            print(name)
    else:
        print('失败')








