import time
import urllib3

x = urllib3.PoolManager()

while(True):
    y = x.request("GET", "http://localhost:8080/status?username=neko").data
    print(y)
    time.sleep(1)
    