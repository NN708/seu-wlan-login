# 东南大学 seu-wlan 一键登录脚本
### One-click login for seu-wlan

# 使用方法 Usage

## Windows, macOS, Linux

Python 脚本可以实现通过命令行登录 seu-wlan。你需要首先安装 Python Requests：

You can log into seu-wlan via CLI using Python script. Firstly, install Python Requests:

```
pip install requests
```

下载 **[login.py](https://github.com/NN708/seu-wlan-login/blob/master/Python/login.py?raw=true)** 并使用 Python 运行：

Download **[login.py](https://github.com/NN708/seu-wlan-login/blob/master/Python/login.py?raw=true)** and run it using Python:

```
python login.py
```

## iOS

iOS 脚本使用官方的[“快捷指令”应用](https://itunes.apple.com/us/app/id915249334?at=10l64N)制作，可实现在 Widget 或 Siri 中一键登录 seu-wlan 的功能。

The script for iOS is made with [iOS Shortcuts](https://itunes.apple.com/us/app/id915249334?at=10l64N), to log into seu-wlan with a single click in Widget or Siri.

使用 Safari 打开 **[seu-wlan-login-zh.shortcut](https://github.com/NN708/seu-wlan-login/blob/master/iOS-Shortcuts/seu-wlan-login-zh.shortcut?raw=true)**，选择“拷贝到‘快捷指令’”。打开“快捷指令”应用后，选择“获取快捷指令”，再按指示输入用户名和密码，之后就可以使用该脚本进行登录了。

Open **[seu-wlan-login-en.shortcut](https://github.com/NN708/seu-wlan-login/blob/master/iOS-Shortcuts/seu-wlan-login-en.shortcut?raw=true)** in Safari. Then press ‘Copy to Shortcuts’. After Shortcuts app is opened, press ‘Get Shortcut’. Then input your username and password. The script will work normally after the configuration.