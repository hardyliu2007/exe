# coding: UTF-8
import requests
from tkinter import *
import urllib, time


def download():
    headers = {
        'Host': 'music.163.com',
        'Referer': 'https://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }

    ID = entry.get()
    NAME = ID
    text.insert(END, "正在下载：%s" % ID)
    url='https://music.163.com/song/media/outer/url?id='
    req=requests.get(url+ID,headers=headers,allow_redirects=False, stream=True)
    music_link=req.headers['Location']
    urllib.request.urlretrieve(music_link,NAME + ".mp3")
    text.insert(END, "已下载完成%s" % ID)


root = Tk()
root.title("网易云音乐下载器")
root.geometry("550x400+550+230")

label = Label(root, text="歌曲ID", font=('宋体', 15))
label.grid()

entry = Entry(root, font=('微软雅黑', 20))
entry.grid(row=0, column=1)

text = Listbox(root, font=("微软雅黑", 15), width=45, height=10)
text.grid(row=1, columnspan=2)

button = Button(root, text="开始下载", font=("微软雅黑", 15), command=download)
button.grid(row=2, column=0, sticky=W)

button1 = Button(root, text="退出", font=("微软雅黑", 15), command=root.quit)
button1.grid(row=2, column=1, sticky=E)

mainloop()