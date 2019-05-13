# -*- coding:utf-8 -*-

import numpy as np

print('生成的全零(3,4)數組為:\n',np.zeros((3,4)))
print('生成的對角線為1的數組為:\n',np.eye(3))
print('生成的對角線為1,2,3,4的數組為:\n',np.diag([1,2,3,4]))
print('生成的0~7數組為:\n',np.arange(8))
print('生成的0~1 10個線性數組為:\n',np.linspace(0,1,10))
