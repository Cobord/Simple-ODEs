import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

mu = 3.0

def van_der_pol_oscillator_deriv(x, t):
    nx0 = x[1]
    nx1 = -mu * (x[0] ** 2.0 - 1.0) * x[1] - x[0]
    res = np.array([nx0, nx1])
    return res

def van_der_pol_oscillator_deriv2(x,t):
    nx0=x[0]
    ny0=x[1]
    npx0=x[2]
    npy0=x[3]
    res=np.array([npy0,npx0-mu*(1-nx0**2)*ny0,-ny0-2*mu*nx0*ny0*npy0,-nx0+mu*npy0-mu*nx0**2*npy0])
    return res

ts = np.linspace(0.0, 50.0, 500)

xs = odeint(van_der_pol_oscillator_deriv, [4.0, 4.0], ts)
plt.plot(xs[:,0], xs[:,1])
plt.gca().set_aspect('equal')
plt.savefig('vanderpol_oscillator.png')
plt.show() 

xs = odeint(van_der_pol_oscillator_deriv2, [4.0, 0.0,0.0,4.0], ts)
plt.plot(xs[:,0], xs[:,3])
plt.gca().set_aspect('equal')
plt.savefig('vanderpol_oscillator2.png')
plt.show() 

plt.plot(ts,xs[:,0])
plt.savefig('vanderpol_oscillator2_time.png')
plt.show()
