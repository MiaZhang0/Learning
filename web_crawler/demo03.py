#获取历史天气数据,动态网页必用正则表达式
import requests
import re
import pandas as pd

url = r'http://tianqi.2345.com/t/wea_history/js/202002/58362_202002.js'
respones = requests.get(url)
#查看返回状态码是否是200
# print(respones)
res = respones.text

#获取日期
date = re.findall("ymd:'([\d-]+)',",res)
#获取最高温度
Mtmp = re.findall("bWendu:'([\d-]+℃)',",res)
#获取天气状况
tianqi = re.findall("tianqi:'(.*?)',",res)
#获取空气质量
aqiInfo = re.findall("aqiInfo:'(.*?)',",res)
#将结果构造为字典
dict = {'date':date,'Mtmp':Mtmp,'tianqi':tianqi,'aqiInfo':aqiInfo}
#将字典转换为表格
frame = pd.DataFrame(dict)
pd.set_option('display.max_rows',31) #设置最大显示行数
pd.set_option('display.max_columns',5) #设置最大显示列数
# pd.set_option('display.width',50) #设置显示宽度
pd.set_option('display.unicode.ambiguous_as_wide', True) #设置对齐
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('expand_frame_repr', False) #不换行

print(frame)
