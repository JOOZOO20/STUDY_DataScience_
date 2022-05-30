import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-10,10,1001)
FX=np.zeros_like(X)

'''
 FX=np.zeros_like(X) 를 사용한이유
 : x와 같은 크기의 튜플을 만들고 초기화가지 하기 위해 사용
'''

def function(x):
    if  x<0:
        return 0
    if x>=0:
        return 1

for i in range(0,1001):
    FX[i]=function(X[i]) # i=1000일 때는 10이라는 값 들어있음.

plt.plot(X,FX,'o') # 선으로 긋지말고 점으로 일일히 다 찍어라.
plt.show()

#mfc=marker face color