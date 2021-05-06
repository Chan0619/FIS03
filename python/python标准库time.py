import time

print(time.asctime())
print(time.time())
print(time.localtime())  # 生成元祖形式
# time.struct_time(tm_year=2021, tm_mon=4, tm_mday=21, tm_hour=21, tm_min=16, tm_sec=46, tm_wday=2, tm_yday=111, tm_isdst=0)
print(time.strftime('%Y年%m月%d日 %H:%M:%S', time.localtime()))

# 获取两天前的时间
now_timestamp = time.time()  # 获取当前时间戳
two_day_before = now_timestamp - 2 * 24 * 60 * 60  # 两天前时间戳
time_tuple = time.localtime(two_day_before)
print(time.strftime('%Y-%m-%d %H:%M:%S', time_tuple))
