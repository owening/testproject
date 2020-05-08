import urllib.request
import math
respone = urllib.request.urlopen("http://www.baidu.com")
print(respone.status)
print(respone.read())
print(respone.headers)

print(math.ceil(6.6))
print(math.floor(5.1))
print(math.sqrt(36))