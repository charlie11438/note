# -*- coding:utf-8 -*-

import numpy as np

a=np.array([1,2,3,4])
b=np.array([[0,0,0,0],[1,1,1,1],[2,3,4,5]])

print('生成的數組1為:\n',a)
print('生成的數組2為:\n',b)
print('生成的數組1形狀為:',a.shape)
print('生成的數組2形狀為:',b.shape)

print('兩者相加為:\n',a+b)
print('兩者相加的shape為:',(a+b).shape)
