import time

# print(time.asctime())
# print(time.time())
# print(time.localtime())
#
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#获取两天前时间
now_timestamp = time.time()
two_day_before = now_timestamp - 60*60*24*2
time_tuple = time.localtime(two_day_before)
print(type(time_tuple))
print(time.strftime("%Y/%m/%d %H:%M:%S", time_tuple))