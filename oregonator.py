import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

krates = [.656, 52.224, 32.768, 10.496, 8.192] 
fval = .2

def oregonator_deriv(x,t):
    resx=krates[0]*x[3]*x[1] - krates[1]*x[0]*x[1]+krates[2]*x[3]*x[0]-2*krates[3]*x[0]**2
    resy=-krates[0]*x[3]*x[1] - krates[1]*x[0]*x[1]+.5*krates[4]*fval*x[4]*x[2]
    resz=2*krates[2]*x[3]*x[0] - krates[4]*x[4]*x[2]
    return np.array([resx,resy,resz,0,0])

ts = np.linspace(0.0, 5.0, 500)
xin = [1.0, 5.0,1.0,2.0,2.0]

xs = odeint(oregonator_deriv,xin, ts)
plt.plot(xs[:,0], xs[:,1])
plt.gca().set_aspect('equal')
plt.savefig('oregonatorXY.png')
plt.show()

plt.plot(ts,xs[:,0],label='$X$')
plt.plot(ts,xs[:,1],label='$Y$')
plt.plot(ts,xs[:,2],label='$Z$')
plt.legend(loc='best')
plt.savefig('oregonator_time.png')
plt.show()