import numpy as np
import matplotlib.pyplot as plt

n=np.linspace(-100,100,300)
x=np.linspace(-2,2,300)
fx=(x**(2*n+1)) / (1+x**(2*n))
plt.plot(x,fx)
plt.show()