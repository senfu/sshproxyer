import tkinter
import tkinter.font as tf
from os import system, popen, chmod
from sys import exit

HOST = '127.0.0.1'
USER = 'user'


def start():
    if B['text'] == '开启':
        print('start')
        Info['text'] = '\n'
        system('start .\\bin\\ssh -vfND localhost:2080 '+USER+'@'+HOST+' -o ServerAliveInterval=30 -i .\\res\\id_rsa')
        system('start .\\bin\\sysproxy.exe global socks=127.0.0.1:10808 "localhost;127.*;10.*;172.16.*;172.17.*;172.18.*;172.19.*;172.20.*;172.21.*;172.22.*;172.23.*;172.24.*;172.25.*;172.26.*;172.27.*;172.28.*;172.29.*;172.30.*;172.31.*;192.168.*;127.0.0.1"')
        Info['text'] = Info['text'] + '系统代理已开启\n'
        system('start .\\bin\\v2ray\\wv2ray.exe')
        Info['text'] = Info['text'] + 'v2ray已启动\nSSH已启动\n'
        B['text'] = '关闭'
    elif B['text'] == '关闭':
        print('shutdown')
        Info['text'] = '\n'
        system('start .\\bin\\sysproxy.exe set 1 ---')
        Info['text'] = Info['text'] + '系统代理已取消\n'
        output = popen('tasklist|findstr /i "wv2ray.exe"').read()
        while output != '':
            system('tasklist|findstr /i "wv2ray.exe" && taskkill /f /im "wv2ray.exe"')
            output = popen('tasklist|findstr /i "wvray.exe"').read()

        output = popen('tasklist|findstr /i "ssh.exe"').read()
        while output != '':
            system('tasklist|findstr /i "ssh.exe" && taskkill /f /im "ssh.exe"')
            output = popen('tasklist|findstr /i "ssh.exe"').read()
        Info['text'] = Info['text'] + 'v2ray已关闭\nSSH已关闭'
        B['text'] = '开启'

def on_closing():
    print('exit')
    Info['text'] = '再见！'
    system('start .\\bin\\sysproxy.exe set 1 ---')
    output = popen('tasklist|findstr /i "wv2ray.exe"').read()
    while output != '':
        system('tasklist|findstr /i "wv2ray.exe" && taskkill /f /im "wv2ray.exe"')
        output = popen('tasklist|findstr /i "wvray.exe"').read()

    output = popen('tasklist|findstr /i "ssh.exe"').read()
    while output != '':
        system('tasklist|findstr /i "ssh.exe" && taskkill /f /im "ssh.exe"')
        output = popen('tasklist|findstr /i "ssh.exe"').read()
    exit(0)
    
    

system("cacls .\\res\\id_rsa /t /p %USERNAME%:F < .\\res\\y.txt")
top = tkinter.Tk()
top.geometry('300x300')
top.title("SSHproxyer")
top.iconbitmap('.\\res\\sshproxyer.ico')
top.protocol("WM_DELETE_WINDOW", on_closing)

ft = tf.Font(family='微软雅黑', size=15, weight=tf.BOLD)
Label1 = tkinter.Label(top, text="欢迎使用SSHproxyer！", width=20, height=3, font=ft)
B = tkinter.Button(top, text = '开启', command = start)
B['width'] = 10
B['height'] = 2
Info = tkinter.Label(top,text='')
Label1.pack()
B.pack()
Info.pack()
top.mainloop()