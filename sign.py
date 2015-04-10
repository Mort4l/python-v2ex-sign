#coding:utf-8
import requests,re
class v2ex:
    def sign(self):
        s=requests.Session()
        payload={
            "u":self.u,
            "p":self.p,
            "next":"/",
            "once":re.findall('value="(\d+)" name="once"',s.get("http://www.v2ex.com/signin").text)[0]
            }
        signin=s.post("http://www.v2ex.com/signin",data=payload,headers={'Referer': 'http://www.v2ex.com/signin'})
        if signin.text.find("signout")==-1:
            print self.u+" 登录失败！"
        else:
            try:
                daily=re.findall('(/mission/daily/redeem\?once=\d+)',s.get("http://www.v2ex.com/mission/daily").text)[0]
                a=s.get("http://www.v2ex.com"+daily,headers={"Referer":"http://www.v2ex.com/mission/daily"})
                print self.u+" 签到成功！"
            except:
                print self.u+" 签到失败！"
    def __init__(self,u,p):
        self.u=u
        self.p=p
sign1=v2ex("UsernNme","PassWord")
sign1.sign()
