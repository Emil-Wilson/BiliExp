# -*- coding: utf-8 -*-
from models.Biliapi import BiliWebApi
from models.PushMessage import PushMessage
import json
def main(*args):
    with open('config/config.json','r',encoding='utf-8') as fp:
        configData = json.load(fp)

    pm = PushMessage(configData["SCKEY"], "B站经验脚本账户有效性检查")

    for x in configData["cookieDatas"]:
        try:
            biliapi = BiliWebApi(x)
            print(f'id为{x["DedeUserID"]}的账户验证有效')
        except Exception as e: 
            pm.addMsg(f'id为{x["DedeUserID"]}的账户登录验证失败,原因为{str(e)}。')

    msg = pm.getMsg()
    if msg:
        print(msg)
        try:
            info = pm.pushMessage()
            print(f'消息推送信息为{str(info)}')
        except Exception as e: 
            print(f'消息推送异常，原因为{str(e)}。')
    else:
        print(f'没有账号失效消息')

if __name__=="__main__":
    main()