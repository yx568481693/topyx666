#	-*-	coding:	utf-8	-*-
import urllib2
import requests
import os
from config import UPDATE_URL
#from bruter import scanSite

#输入一个文件名
os.dir()

Method = "cmsdict.txt"
url = UPDATE_URL + Method

#建立一个字典
list1 = []
print url
with open(url) as f:
    poc = f.readline()
    while poc:
        list1.append(poc)
        poc = f.readline()
