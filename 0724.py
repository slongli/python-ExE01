# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:13:04 2018

@author: Administrator
"""
#list
a=['him',25,100,'her',100,25]
print(a)

a[1:3]

a=[1,2,3,4,5]
a+[6,7,8]

a=[1,2,3,4,5,6]
a[0]=9
a[2:5]=[12,14,15]
a

a[2:5]=[] #删除

25 in a

9 in a

set([9,15]) <= set(a)

#tuple

a = (1991,2014,'physics','math')
print(a,type(a),len(a))

tup=(1,2,3,4,5,6)
print(tup[0],tup[1:5])

tup[0]=11#'tuple' object does not support item assignment

tup1 = ()
tup2 = (20,)
tup2 = (20)

tup1,tup2 = ((1,2,3),(4,5,6))
print(tup1+tup2)

#set

student = {'tom','jim','mary','tom','jack','rose'}
print(student)

'rose' in student
'ken' in student

a = set('abracadabra')
b = set('alacazan')
a
b

a - b#把b中有的a中的去掉
a|b#
a&b#共同的
a^b#除了相同的

a=['him',25,100,'her',100,25]
set([25,100]) <= set(a)

#dic
dic = {}
tel = {'Jack':1557,'Tom':1320,'Rose':1886}
tel

tel['Jack']

del tel['Rose']
tel

tel['Mary'] = 4127
tel

list(tel.keys())
sorted(tel.keys())

'Tom' in tel

'Mary' not in tel

dict([('space',4139),('guido',4127),('jack',4008)])

dict(space=4139,guido=4127,jack=4008)


#Pandas
from pandas import Series
x = Series(['a',True,1],index=['first','second','third'])
x = Series(['a',True,1])

x[1]

x['second']

x.append('2')#不能追加单个元素

n=Series(['2'])
x.append(n)


1 in x#false

1 in x.values#true

x[1:3]

x[[0,2,1]]

x.drop(0)#不行
x.drop('first')

x.drop(x.index[1])

x['a'!=x.values]

#DataFrame

from pandas import DataFrame


df=DataFrame({
        'age':[21,22,23],
        'name':['KEN','John','JIMI']
        })

df=DataFrame({
        'age':[21,22,23],
        'name':['KEN','John','JIMI']
        },index=['first','second','third'])


df['age']

df[1:2]

df.iloc[0:1,0:1]#[行，列]

df.iloc[1,1]#[行，列]

df.at['first','name']
df.at[0,'name']

df.columns

df.columns=['age2','name2']

df.index
df.index=range(1,4)
df.index

df.drop(1,axis=0)#axis=0 按行删除
df.drop('name2',axis=1) #按列删除

del df['age2']
       

#增加行，注意，这种方法，效率非常低，不应该用于遍历中
df.loc[len(df)] = [24,"KENKEN"]
df.loc['ge']=[24,"fefe"]

#增加列
df['newColumn']=[2,4,6,8,10,7]


"""
if 判断条件：
    执行语句……
else：
    执行语句……
"""

flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print('welcome boss')    # 并输出欢迎信息
else:
    print(name)              # 条件不成立时输出变量名称
    
    
    
num = 5     
if num == 3:            # 判断num的值
    print('boss')        
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:           # 值小于零时输出
    print('error')
else:
    print('roadman')     # 条件均不成立时输出

if num==3:
    print('boss')
else:
    if num<0:
        print('lala')
    else:
        print('roadman')




