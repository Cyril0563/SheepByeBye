'''
#Python羊了个羊补丁注入
#开源地址：https://github.com/Cyril0563/SheepByeBye
#作者：Cyril0563
#时间：2022-09-20
'''





import requests
import os
import time
url = "https://raw.iqiq.io/Cyril0563/SheepByeBye/main/Api/sheep.json"
# 路径地址： C:\Users\Cyril\Documents\WeChat Files\wxid_0vdbn75c9v2o22

# ***版本更新代码开始***
l_ver = '1.5' #本地软件版本号
#获取服务器API数据
r = requests.get(url)
if r.status_code == 200:
    # print(r.status_code)#返回服务器状态码
    # print(r.text)
    # print("服务器下载地址：" + r.json()['down_url'])
    s_ver = r.json()['ver'] #获取服务器版本
else:
    print("网络错误,错误代码：" + r.status_code)
    # print(r.status_code)返回服务器错误状态码

#比较版本号
if l_ver < r.json()['ver']:
    print("发现新版本，正在更新中……请稍后！")
    # 下载新版本
    r = requests.get(r.json()['down_url'])
    # 保存拜拜羊了个羊.exe
    with open("拜拜羊了个羊.exe", "wb") as code:
        code.write(r.content)
    print("更新完成！")
    # 重启软件
    os.system("拜拜羊了个羊.exe")
    time.sleep(1)
    exit(0)

else:
    print("*" * 25)
    print("项目开源地址：github.com/Cyril0563/SheepByeBye")
    print("公众号：源享家")
    print("当前版本：" + l_ver)
    print("当前版本是最新版本，无需更新！")
    print("*" * 25)
    # 3秒后清除屏幕
    time.sleep(3)
    os.system('cls')
# ***版本更新代码结束***



# ***主程序代码开始***
print("路径获取教程：电脑端微信-左下角更多-设置-文件管理-打开文件夹-弹出的文件夹路径全地址")
WeChat_Path = input("请输入微信文件夹路径：")
App_Path = WeChat_Path + '/Applet/wx141bfb9b73c970a9/usr/gamecaches/resources'
# 将路径中的\\全部替换成/
App_Path = App_Path.replace('\\', '/')
# 判断当前路径是否存在
if os.path.exists(App_Path):
    # 获取文件夹里文件大小为1025字节的json文件
    for root, dirs, files in os.walk(App_Path):
        for file in files:
            if os.path.getsize(App_Path + '/' + file) == 1025:
                print("已获取到文件：" + file)
                # 打开获取到的json文件
                with open(os.path.join(root, file), 'r') as f:
                    # 读取json文件内容
                    data = f.read()
                    print("本地文件内容获取成功！")
                    # 获取服务器内容
                    r = requests.get(url)
                    KEY_URL = r.json()['KEY_JSON']
                    KEY_CONTENT = requests.get(KEY_URL).text
                    print("服务器文件内容获取成功！")
                    # 将服务器内容写入文件
                    with open(os.path.join(root, file), 'w') as f:
                        f.write(KEY_CONTENT)
                        print("最新补丁植入成功！请重新运行羊了个羊小程序！")
                        time.sleep(3)
                        exit(0)
            elif file == files[len(files)-1]:
                print("未知错误！请自行复制下方的路径并删除文件夹后重新运行本程序！")
                Error_Path = WeChat_Path + '\Applet\wx141bfb9b73c970a9'
                print(Error_Path)
                # 输出10秒中的格子进度条
                for i in range(10):
                    print('程序将在10秒后自动退出！', '█' * i, end='')
                    time.sleep(1)
                    print('\r', end='')
                exit(0)
else:
    print("未检测到羊了个羊小程序！请运行一次羊了个羊小程序后再试！")
    time.sleep(3)
    pass
# ***主程序代码结束***

