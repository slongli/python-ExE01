# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:46:28 2018

@author: Administrator
"""

a=4.2;
b=3.4;
a+b

(a+b)==7.6

from decimal import Decimal
a=Decimal('4.2')
b=Decimal('3.4')
a+b
print(a+b)
(a+b)==Decimal('7.6')

string = "I am Lislong"
string.find("am")
string.find("boy")

import re
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python',text,flags=re.IGNORECASE)

text='yeah,but no,but yeah,but no,but yeah'
text.replace('yeah','yep')

text='UPPER PYTHON, lower python, Mixed Python'
re.sub('python','snake',text,flags=re.IGNORECASE)

parts=['IS','chicage','Not','Chicage?']
' '.join(parts)


','.join(parts)