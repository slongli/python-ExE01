# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:25:32 2018

@author: Administrator
"""

# 不带参数的函数
def printLine():
   #输出一条横线
   print("--------------------------------------------");
   #没有返回值
   #return;

printLine();
         
def IloveMara(name,age):
    print("name is:",name,"age is:",age)
    return;


IloveMara(age=22,name='Mara')
IloveMara('Mara',22)

#错误调用
IloveMara('Ken')

# 默认参数的函数
def printInfo(name, age=20):
   print("name is: ", name, "; age is: ", age);
   #没有返回值
   return;
 
#正确调用
printInfo("KEN");
printInfo("Mara",22);       

         
def printInfo(name,*args):
    print('name is',name)
    printLine()
    for arg in args:
        print(arg)
    return;
 
    
printInfo("Mara",22,"女",156,"aishenglong")
        
         
def printInfo(name, **kvArgs):
   #打印任何传入的字符串
   print("name is: ", name);
   printLine();
   for k in kvArgs:
       print(k, "is: ", kvArgs[k]);
   #没有返回值
   return;
 
#正确调用
printInfo("KEN", age=20, sex="男", height="178", weight="70KG");         
#错误调用
printInfo("KEN", 20, "男");

#有返回值的函数
def maxValue(*args):
    rValue = args[0]
    for var in args:
        if rValue < var:
            rValue = var
    return rValue
    

print(maxValue(4,5,2,6,7,2))         
         

import numpy
from pandas import DataFrame
df = DataFrame({
    'key1': ['a','a','b','b','a'],
    'key2': ['one','two','one','two','one'],
    'data1': numpy.random.randn(5),
    'data2': numpy.random.randn(5)
        })

df.groupby('key1')['data1','data2'].agg(lambda arr:arr.max()
- arr.min())
       
#生成一个整数的等差序列
#局限，只能用于遍历

r1_10 = range(1,10,2)

for i in r1_10:
    print(i)

r1_10 = range(0.1,10.1,2)  #不能有小数   
         
             
#生成一个小数的等差序列
import numpy
numpy.arange(0.1,0.5,0.01)

r = numpy.arange(0.1,0.5,0.01)  

#向量化计算，四则运算
r+r
r-r
r*r
r/r          
             
#长短不一时
r + 1             
             
#函数的向量化计算
numpy.power(r,5)
#向量化运算，比较运算
r>0.3
#结合过滤进行使用
r[r>0.3]           

#矩阵运算
numpy.dot(r,r.T)          
             
sum(r*r)
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         