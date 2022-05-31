import sympy as sp

# (a)
x=sp.Symbol('x') #Symbol :x라는 문자 자체를  symbol(변수)로 정의하겠다는 뜻임
fx=(2*x-1)**4
print("(a) answer is ",sp.diff(fx,x))  #diff는 미분하는 함수임. diff(수식, 미분할 변수 대상)

#(b)
x=sp.Symbol('x')
gx=1/(3-x**3)
print("(b) answer is ",sp.diff(gx,x))

#(c)
x=sp.Symbol('x')
fx1=sp.log(sp.tan(x))
print("(c) answer is ", sp.diff(fx1,x))
print("답은?? : ",sp.simplify(sp.diff(fx1,x)))

#(d)
x=sp.Symbol('x')
gx1=sp.exp(sp.sqrt(x))
print('(d) answer is ',sp.diff(gx,x))