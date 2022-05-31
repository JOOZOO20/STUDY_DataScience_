import sympy as sp

# # sp.facter(수식) // 수식을 인수분해 해주는 함수

# x=sp.Symbol('x')
# fx=sp.exp(2*x)*sp.sin(3*x)
# primefx=sp.diff(fx,x)
# prime2fx=sp.diff(primefx,x)
# k=sp.Symbol('k')
# result = prime2fx+k*primefx+13*fx
# result2 = sp.factor(result)
# print(result2)

#last problem
x=sp.Symbol('x')
fx=sp.exp(x)*sp.sin(x)-x*sp.exp(x)+sp.exp(2*x)
print('이전: ',fx)
print('이후: ',sp.simplify(fx)) #simplify : 수식을 가장 간단하게 나타내주는 함수