from datetime import datetime
import sys
import time

#当前时刻距离元旦有多少秒钟？

# now = datetime.now() #当前时刻
# print(now)
# new_year = datetime(now.year+1,1,1,0,0,0) #下一个元旦的零时
# print(new_year)
# delta = new_year - now #计算时间间隔
# print(delta)
# print(type(delta))
# resp = delta.total_seconds() #获取时间间隔的总秒数
# print(resp)

#当前时刻距离除夕有多少秒钟，并实时倒计时
now = datetime.now()
spring = datetime(now.year+1,1,24,0,0,0)  #除夕的零时
i = 0
while i < 5:
    # pass
    delta = spring - now #时间间隔
    print(delta)
    day = delta.days  #剩余天数
    print(day)
    second = delta.seconds #剩余秒数
    print(second)
    #将秒数换算成时分秒
    sec = second%60  #秒
    print(sec)
    minute = second/60%60  #分
    print(minute)
    hour = second/60/60  #小时
    print(hour)
    if hour>24:
        hour = hour - 24 #如果超过24小时，就算超过1天，所以减去24
        sys.stdout.write("离今年春节还有"+str(day)+"天"+str(hour)+"小时"+str(minute)+"分钟"+str(sec)+"秒"+"\r")
        # sys.stdout.write("离今年春节还有 %d 天 %d 小时 %d 分钟 %d 秒 \r " %(day,hour,minute,sec))
        sys.stdout.flush()
        time.sleep(1)
    i += 1

