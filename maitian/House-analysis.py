#__author:  Stanley

# 根据spider爬取的住房数据进行可视化分析

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import re

pf = pd.read_csv("../maitian2019-01-30.csv",names=['district','title','totalprice','uniprice','size'])
# 将爬取的pf['uniprice']对象的字符元素转换为Series对象的整数元素
uniprice_list = []
for item in pf['uniprice']:
    uniprice = re.findall(r'\'(.*)\'',item)
    uniprice_list.append(int(uniprice[0]))
uniprice_series = pd.Series(uniprice_list)
################################################################
# 将爬取的pf['district']对象的每个字符元素剔除引号之外的内容
district_list = []
for item in pf['district']:
    district = re.findall(r'\'(.*)\'',item)
    district_list.append(district[0])
pf['district'] = pd.Series(district_list)
################################################################
gp1 = uniprice_series.groupby(pf['district'])

########################################################################################################################
# 生成垂直条形图,分析北京各区域平均房价
plt.figure(figsize=(10,6))
plt.rc('font',family='SimHei',size=13)
plt.bar(gp1.mean().index,gp1.mean().values)
plt.title(u'北京各区域二手房房价')
plt.xlabel(u'北京区域')
plt.ylabel(u'每平米平均房价')
plt.show()

########################################################################################################################

# # 生成饼图,分析北京各区域销售的房子占比
pf_district_count = pf.groupby('district')['totalprice'].count()
# print(pf_district_count,type(pf_district_count))
plt.figure(figsize=(10,8))
plt.rc('font',family='SimHei',size=13)
explode = [0]*len(pf_district_count)
explode[5] = 0.05
plt.title(u'北京各区域二手房数量占比')
plt.pie(pf_district_count,labels=pf_district_count.index,explode=explode,shadow=False,autopct='%1.1f%%',radius=1)
plt.axis('equal')
plt.show()
########################################################################################################################



