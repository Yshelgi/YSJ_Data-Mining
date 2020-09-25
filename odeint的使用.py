from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def diff(y,x):
    return x

def diff2(y,t):
    v,a=y
    return np.array([1/2*t,v])

x=np.linspace(0,10,100)
t=np.linspace(0,10,100)

res1=odeint(diff2,[0,0],t)
res=odeint(diff,0,x)
print(res)
plt.figure()
plt.plot(x,res,'b',label=r'$ \frac{dy}{dx}=x$')
plt.legend()
plt.grid()
plt.show()


plt.figure()
plt.plot(t,res1[:,0],'b',label=r'$ y(t)$')
plt.plot(t,res1[:,1],'r',label=r'$ v(t)$')
plt.legend()
plt.grid()
plt.show()