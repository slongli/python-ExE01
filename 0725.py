# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:53:06 2018

@author: Administrator
"""

from pandas import Series
from pandas import DataFrame

for i in range(10):
    print('现在是:',i)

for i in range(3,10):
    print(i)
    
#遍历字符串
for letter in 'python':
    print('现在是:',letter)
    
#遍历列表
fruits = ['banana','apple','mango']

for fruit in fruits:
    print('now is:',fruit)
    
#遍历序列

x = Series(['a',True,1],index = ['frist','second','third'])
x[0]
x['second']
x[2]

for i in x.values:
    print(i)

for v in x:
    print("x中的值：",v)
    
for index in x.index:
    print("x中的索引：",index)
    print("x中的值:",x[index])
    print("_____________")
    
#遍历数据框
df = DataFrame({
        'age':Series([21,22,23]),
        'name':Series(['ken','susan','mary'])
        })
    

#遍历列名
for r in df:
    print(r)

#遍历列：
for cName in df:
    print('df中的列：\n',cName)
    print('df中的值：\n',df[cName])
    print('-------------------')

#遍历行，方法一
for rIndex in df.index:
    print('现在是第',rIndex,'行')
    print(df.iloc[rIndex])

#遍历行，方法二

for r in df.values:
    print(r)
    print(r[0])
    print(r[1])
    print("--------------------")


#遍历行，方法三


for index,row in df.iterrows():
    print('第',index,'行：')
    print(row)
    print("--------------------")






















