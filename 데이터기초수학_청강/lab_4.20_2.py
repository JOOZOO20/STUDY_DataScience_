import numpy as np
import matplotlib.pyplot as plt

# 아니 중간에 대체 왜 끊김?
x=np.linspace(-50,50,1001)
gx=1/(1+np.exp(-x))

'''
x=np.linspace(-10,10,1001)
gx=1/(1+np.exp(-x))
'''

plt.plot(x,gx,'o')
plt.show()