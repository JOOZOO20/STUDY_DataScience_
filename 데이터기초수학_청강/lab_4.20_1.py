import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-1,5,1001)
FX=np.zeros_like(X)

def function(x): # w o w... def==define
    if (x>=-1 and x<1):
        return -(x**2)+2
    elif (x>=1 and x<=3):
        return x**2-4*x+3
    elif (x>3 and x<=5):
        return -(x**2)+8*x-14

for i in range(0,1001):
    FX[i]=function(X[i]) 

plt.plot(X,FX,'o') 
plt.show()