# -*- coding:utf-8 -*-

import numpy as np

print('隨機生成常態分配5*4數組為:\n',np.random.randn(5,4))
print('隨機生成均勻分布間隔10的數組為:\n',np.random.uniform(0,1,10))
print('隨機生成10個數組為:\n',np.random.random(10))
print('隨機生成10個隨機整數數組為:\n',np.random.randint(1,10,3))
