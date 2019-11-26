import datetime

#timedelta 用于计算时间间隔的方法
nowtime = datetime.datetime.now()
print(nowtime) #2019-11-27 03:00:05.507890
oneyearlater = datetime.timedelta(weeks=52,minutes=10)  #获取52周10分钟，一年10分以后的时间是多少 #2020-11-25 03:10:05.507890
print(nowtime+oneyearlater)
tenminslater = datetime.timedelta(minutes=10) #获取10分钟后的时间是多少 #2019-11-27 03:10:05.507890
print(nowtime+tenminslater)