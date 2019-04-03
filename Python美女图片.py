#@Time  : 2019/3/26 18:56
#@Author: www.mrchi.cn
#@File  : Python美女图片.py
# -*- coding: UTF-8 -*-
import requests
import re
import time
from  to_mysql  import Insert
#请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
#URL列表
urls=["https://www.dbmeinv.com/index.htm?cid=2&pager_offset={}".format(str(i)) for i in range(1,203) ]
#路径，可以更改成你的路径
path='G:\Python爬虫文件夹\mn1\\'
#获取图片并写入本地文件
def get_girlphoto(url):
    try:
        data = requests.get(url, headers=headers)
        # print(data.text)
        pattern = re.compile('<img class.*?title="(.*?)".*?src="(.*?)"')
        content=re.findall(pattern,data.text)
        for title,urls in content:
            print(urls+title)
            Insert(urls,title)
    except :
        print("Exception")
if __name__ == '__main__':#主函数
    #循环URL
    for url in  urls:
        # print(url)
        # time.sleep(1)
        get_girlphoto(url)

