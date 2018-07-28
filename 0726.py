# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:12:53 2018

@author: Administrator
"""
from pandas import Series
from pandas import DataFrame

#最普通的while循环
i = 0
while i <= 9:
   print('遍历到 :', i);
   i = i+1;
   
#整合if判断语句，使用continue
i = 1
while i < 10:   
    i += 1              # i = i + 1
    if i%2 != 0:         # 非双数时跳过输出
        continue
    print(i)            # 输出双数2、4、6、8、10

#整合if判断语句，使用break
i = 1
while True:             # 循环条件为1必定成立
    print(i)            # 输出1~10
    i += 1
    if i > 10:          # 当i大于10时跳出循环
        break

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
df = DataFrame({
        'age':Series([21,22,23]),
        'name':Series(['KEN','John','JIMI'])
        })
    
rowCount = len(df)

i = 0

while i<rowCount:
    print(df.iloc[i])
    i=i+1
    print('-------------------')