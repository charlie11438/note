# -*- coding:utf-8 -*-

import numpy as np # 導入模組

a=np.array([[2,3],[4,5]])

print('產生的ndarray為:\n',a)
print('產生的ndarray大小為:',a.size)
print('產生的ndarray維度為:',a.ndim)
print('產生的ndarray形狀為:',a.shape)
print('產生的ndarray型態為:',a.dtype)

b=np.array([[2,3,4],[5,6,7],[8,9,10]],dtype='float64')
print('第二個產生的ndarray為:\n',b)

c=b.reshape((1,9))
print('重新塑成(1,9)的ndarray為:\n',c)
