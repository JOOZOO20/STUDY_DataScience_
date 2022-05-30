from lib2to3.pgen2.pgen import DFAState
import numpy as np
import matplotlib.pyplot as plt

# (n,an)을 나타냄
n=[]
an=[]

#(1,109)를 추가함.
n.append(1)
an.append(109)

#an[-1] == an의 리스트에서 맨 마지막 원소 값을 들고 오겠다.
while(an[-1] != 1):
    if(an[-1]%2==0):
        an.append(an[-1]/2)
        n.append(n[-1]+1)
    else:
        an.append(3*an[-1]+1)
        n.append(n[-1]+1)

plt.plot(n,an,'o')
plt.show()
print(n[-1])