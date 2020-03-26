#抓取红牛公司信息
#知识点
# pd.set_option('display.max_columns',a) #a就是你要设置显示的最大列数参数
# pd.set_option('display.max_rows',b) #b就是你要设置显示的最大的行数参数
# pd.set_option('display.width',x) #x就是你要设置的显示的宽度，防止轻易换行

import requests
import re
import bs4
import pandas as pd

url = r'http://www.redbull.com.cn/about/branch'
response = requests.get(url) #返回状态码
res = response.text #返回源代码
# print(response)
# print(res)
company = re.findall('<h2>(.*?)</h2>', res)  #获取公司信息
address = re.findall("<p class='mapIco'>(.*?)</p>", res) #获取公司地址

soup = bs4.BeautifulSoup(res, features='html.parser')#将源代码转换成汤对象
# print(soup)
# for i in soup.findAll(name= 'p',attrs={'class':'mailIco'}):
#     print(i.text)

#列表表达式
mail = [i.text for i in soup.findAll(name='p', attrs={'class': 'mailIco'})]
tell = [i.text for i in soup.findAll(name='p', attrs={'class': 'telIco'})]

dict = {'company': company, 'address': address, 'mail': mail, 'tell': tell}
frame = pd.DataFrame(dict)
pd.set_option('display.max_rows',50) #设置最大显示行数
pd.set_option('display.max_columns',5) #设置最大显示列数
pd.set_option('display.width',500) #设置显示宽度
pd.set_option('display.max_colwidth',500) #设置打印宽度，有他没有···
pd.set_option('display.unicode.ambiguous_as_wide', True) #设置对齐
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('expand_frame_repr', False) #不换行
print(frame)
frame.to_html('redbull_Infofile.html') #将结果以html表格的方式展示
