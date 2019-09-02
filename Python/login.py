import requests
import re
import json
import base64

config_file = 'config.json'
pattern = re.compile(r'\{.*\}')

r = requests.get('http://202.119.25.2/drcom/chkstatus?callback=dr1002')
if r.status_code != 200:
    print('错误：连接失败。')
    exit()
status = json.loads(pattern.findall(r.text)[0])

if status['result'] == 1:
    print('错误：你已经登录了 seu-wlan。')
    exit()
elif status['result'] != 0:
    print('错误：未知错误。')
    exit()

try:
    with open(config_file) as f:
        config = json.load(f)
except IOError:
    print('错误：配置文件 config.json 不存在。')
    with open(config_file, 'w') as f:
        config = {
            'username': '',
            'password': ''
        }
        json.dump(config, f, indent=2)
        exit()

if config['username'] == '' or config['password'] == '':
    print('错误：请在配置文件 config.json 中填写用户名及密码。')
    exit()

login_url = 'http://202.119.25.2:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C0%2C' + config['username'] + '&user_password=' + config['password'] + '&wlan_user_ip=' + status['v46ip'] + '&wlan_ac_name=jlh_me60'
r = requests.get(login_url)
if r.status_code != 200:
    print('错误：连接失败。')
    exit()
login = json.loads(pattern.findall(r.text)[0])

if login['result'] != 1:
    message = base64.b64decode(login['msg']).decode()
    if message == 'ldap auth error':
        print('错误：用户名或密码错误。')
    elif message == 'userid error1':
        print('错误：用户名不存在。')
    elif message == 'userid error2':
        print('错误：密码错误。')
    else:
        print('错误：登录失败。')
    exit()

print('登录成功。')