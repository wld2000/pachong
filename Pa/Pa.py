import json
import requests
import os
url = "https://img0.baidu.com/it/u=2548914342,2177261678&fm=253&fmt=auto&app=120&f=JPEG"
root = "F://Pachong//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print("文件已经保存")
    else:
        print("文件已经存在")
except:
    print("爬取失败")


