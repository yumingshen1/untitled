import requests
import json

class APIrequest(object):
  #登录
  def msb_api_login(self,url,username,password,width):

    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}

    data = {"username":username,"password":password,"width":width}

    return requests.post(url,headers=headers,data=data)


  #创建线索
  def msb_api_clues(self,url,age,channel,expstatus,flowstatus,sales,sex,status,areaCode,mobile,username):

    headers = {"Content-Type":"application/x-www-form-urlencoded"}

    data = {"age":age,"channel":1,"expstatus":1,"flowstatus":1,"sales":392,"sex":0,
            "status":1,"areaCode":"+216","mobile":"","username":""}
    return requests.post(url,headers=headers,data=data)


  #新建订单
  def msb_api_order(self,url,heard,data):

    return requests.post(url, heard=heard, json=data)


  #获取订单号
  def msb_api_orderid(self,url,heard,data):

    return requests.post(url, heard=heard, json=data)


  #支付
  def msb_api_pay(self,url,heard,data):

    return requests.post(url, heard=heard, json=data)