#coding:utf-8
import requests,re
class v2ex:
    def sign(self):
        s=requests.Session()
        payload={
            "u":self.u,
            "p":self.p,
            "next":"/",
            "once":re.findall('value="(\d+)" name="once"',s.get("https://www.v2ex.com/signin").text)[0]
            }
        signin=s.post("https://www.v2ex.com/signin",data=payload,headers={'Referer': 'httpss://www.v2ex.com/signin'})
        if signin.text.find("signout")==-1:
            print self.u+" 登录失败！"
        else:
            print self.u+" 登录成功！"
            if s.get("https://www.v2ex.com/mission/daily").text.find("fa-ok-sign")!=-1:
                print self.u+" 已领取过奖励!"
            else:
                try:
                    daily=re.findall('(/mission/daily/redeem\?once=\d+)',s.get("https://www.v2ex.com/mission/daily").text)[0]
                    a=s.get("https://www.v2ex.com"+daily,headers={"Referer":"https://www.v2ex.com/mission/daily"})
                    print self.u+" 签到成功！"
                except:
                    print self.u+" 签到失败！"
    def __init__(self,u,p):
        self.u=u
        self.p=p
sign1=v2ex("UsernNme","PassWord")
sign1.sign()
