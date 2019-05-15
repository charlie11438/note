# -*- coding:utf-8 -*-

import numpy as np

a=np.array(range(2,100,3))

print('產生的數組為:\n',a)
print('數組的平均數為:',np.mean(a))
print('數組的標準差為:',np.std(a))
print('數組的變異數為:',np.var(a))
print('數組的最大值為:',np.max(a))
print('數組的最小值為:',np.min(a))
