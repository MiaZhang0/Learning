#抓取链家网站房源信息，该网站是反爬网站，注意带上请求头中的信息
import requests
import bs4
import pandas as pd

url = r'https://sh.lianjia.com/ershoufang/pudong/pg1/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
response = requests.get(url, headers=header)
# print(response)
res = response.text
soup = bs4.BeautifulSoup(res,features='html.parser')
#列表表达式获取房源信息
name = [i.text.strip() for i in soup.findAll(name='a',attrs={'data-el':'region'})] #xx.strip()去空格，获取房源名
# list = [i.text.split('|') for i in soup.findAll(name='div',attrs={'class':'houseInfo'})]

house_type = [i.text.split('|')[0].strip() for i in soup.findAll(name='div',attrs={'class':'houseInfo'})] #字符串分割，获取房源类型
size = [float(i.text.split('|')[1].strip()[:-2]) for i in soup.findAll(name='div',attrs={'class':'houseInfo'})] #字符串切片，获取房源面积
direction = [i.text.split('|')[2].strip() for i in soup.findAll(name='div',attrs={'class':'houseInfo'})]#获取房源朝向
decor = [i.text.split('|')[3].strip() for i in soup.findAll(name='div',attrs={'class':'houseInfo'})]#获取房源装修类型
floor = [i.text.split('|')[4].strip() for i in soup.findAll(name='div',attrs={'class':'houseInfo'})]#获取房源楼层
build_time = [i.text.split('|')[-2].strip() for i in soup.findAll(name='div',attrs={'class':'houseInfo'})]#获取房源年建时间
new_build_time = []
for j in build_time:
    if j.find('年建') < 0: #判断该元素是否是年建时间，如果不是年建时间，则将其置为空值，并且返回新的列表
       j = ''
    new_build_time.append(j)
# print(new_build_time)
build_type = [i.text.split('|')[-1] for i in soup.findAll(name='div',attrs={'class':'houseInfo'})] #获取房源楼型
total_price = [float(i.text[:-1]) for i in soup.findAll(name='div',attrs={'class':'totalPrice'})] #获取房源总价，万元
unit_price = [int(i.text[2:-4]) for i in soup.findAll(name='div',attrs={'class':'unitPrice'})] #获取房源单价，元
#将获取的数据存放于字典中
dict = {'name':name,'house_type':house_type,'size':size,'direction':direction,'decor':decor,'floor':floor,
        'build_time':new_build_time,'build_type':build_type,'total_price':total_price,'unit_price':unit_price}
#将字典转换成表格
frame = pd.DataFrame(dict)
pd.set_option('display.max_rows',100) #设置最大显示行数
pd.set_option('display.max_columns',12) #设置最大显示列数
pd.set_option('display.width',500) #设置显示宽度
pd.set_option('display.unicode.ambiguous_as_wide', True) #设置对齐
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('expand_frame_repr', False) #不换行
print(frame)