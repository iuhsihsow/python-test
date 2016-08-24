#coding=utf-8
import requests
url = 'http://localhost:8080'
path = "C:/projects/GitHub/python-test/upload/test.txt"
print(path)
files = {'file': open(path, 'rb')}
r = requests.post(url, files=files)
print(r.url,r.text)