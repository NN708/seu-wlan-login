import os
import time
import login

def PingTest():
    err = os.system('ping -4 -n 1 www.baidu.com')
    if err:
        return False
    else:
        return True

flag = False

while True:
    if PingTest():
        flag = False
    else:
        if flag:
            print('断开连接……')
            os.system('netsh wlan disconnect')
            time.sleep(5)
            print('尝试重新连接……')
            err = os.system('netsh wlan connect name=seu-wlan')
            if not err:
                time.sleep(30)
                print('正在登录……')
                login.login()
        else:
            print('发现网络异常')
            flag = True
    time.sleep(60)