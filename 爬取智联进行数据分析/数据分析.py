
# coding: utf-8

# In[1]:

from pandas import read_excel
df = read_excel(r'F:\爬虫项目\zhiliantest\数据12.xlsx')
#处理数据为空的数据
SalarySplit = df['薪资'].str.split('-',expand = True)#利用split方法进行数据的切割，expand = True直接变成DataFrame
df['LowSalary'],df['HighSalary'] = SalarySplit[0],SalarySplit[1]#新建两列分别为最低和最高工资
df#显示df
df.isnull().any()#显示数据为空列
df[df.isnull().values == True]#显示数据为空具体数据
df['HighSalary'] = df.HighSalary.fillna('0K')#将HighSalary中的None变成0K
df['待遇'] = df.待遇.fillna('周末双休,五险一金,年底双薪,加班补助,交通补助')#将待遇中空值填充为周末双休,五险一金,年底双薪,加班补助,交通补助
df['LowSalary'] = df['LowSalary'].replace('薪资面议','0K')#将薪资面议替换为0K
df.isnull().any()#显示数据为空列（均为False）
df1 = df.drop_duplicates()#删除重复数据
df1.drop('url', axis=1, inplace=True)
df1.drop('发布时间', axis=1, inplace=True)
#数据格式处理将df['LowSalary'],df['HighSalary']变换为int型方便后续处理
SalarySplits = df1['HighSalary'].str.split('K',expand = True)#将k切割
df1['HighSalary'] = SalarySplits[0].astype('float')#先变成浮点型然后在变成int型
df1['HighSalary'] = df1['HighSalary'].astype('int')
df1['HighSalary'] = df1['HighSalary'].map(lambda x : x*1000)#将K替换掉数据乘1000
SalarySplits1= df1['LowSalary'].str.split('K',expand = True)#将k切割
df1['LowSalary'] = SalarySplits[0].astype('float')#先变成浮点型然后在变成int型
df1['LowSalary'] = df1['LowSalary'].astype('int')
df1['LowSalary'] = df1['LowSalary'].map(lambda x : x*1000)#将K替换掉数据乘1000
df1


# In[21]:

get_ipython().magic('matplotlib inline')
get_ipython().magic('config InlineBackend.figure_format = "retina"')
import matplotlib
import matplotlib.pyplot as plt
#设置中文字体
font = {'family': 'SimHei'}
matplotlib.rc('font', **font)
#df2['公司类型'].value_counts()
fig = plt.figure(figsize = (8, 8))
CompanyNature_Count = df1['公司类型'].value_counts()
colors  = ["yellow","orange","pink","coral","blue","greenyellow","red","darkseagreen"]  
p_text = plt.pie(CompanyNature_Count, autopct = '%.2f%%', labels = CompanyNature_Count.index,colors=colors)
'''
参数说明：
x  (每一块)的比例，如果sum(x) > 1会使用sum(x)归一化
labels  (每一块)饼图外侧显示的说明文字
explode (每一块)离开中心距离
startangle  起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起
shadow  是否阴影
labeldistance label绘制位置,相对于半径的比例, 如<1则绘制在饼图内侧
autopct 控制饼图内百分比设置,可以使用format字符串或者format function'%1.1f'指小数点前后位数(没有用空格补齐)
pctdistance 类似于labeldistance,指定autopct的位置刻度
radius  控制饼图半径
'''
plt.title('python岗位中各类型企业所占比例', fontsize=24)
plt.show
plt.savefig("最新饼状图.jpg")


# In[22]:

get_ipython().magic('matplotlib inline')
get_ipython().magic('config InlineBackend.figure_format = "retina"')
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
CompanySize_Count = df1['公司人数'].value_counts()#源数据
index = np.arange(len(CompanySize_Count))
fig = plt.figure(figsize = (8, 6))#构造画布
plt.barh(index,CompanySize_Count, tick_label = CompanySize_Count.index,height= 0.8,alpha=0.8,align ='center')
plt.title('python岗位各公司规模总数分布条形图', fontsize = 24)
##plt.yticks(index+0.5,CompanySize_Count.index)
for x,y in enumerate(CompanySize_Count):
 plt.text(y+0.5,x, '%s'%y, va = 'center')
plt.show
plt.savefig('最新横向条形图.jpg')


# In[ ]:




# In[ ]:



