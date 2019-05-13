# -*- coding:utf-8 -*-

import numpy as np

a=np.array(range(8)).reshape((2,4))

print('生成的數組為:\n',a)
print('橫向分割為:\n',np.hsplit(a,2))
print('縱向分割為:\n',np.vsplit(a,2))
print('橫向分割(使用split)為:\n',np.split(a,2,axis=1))
