import time
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
time.sleep(1)#暂停一秒后再次输出时间
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
