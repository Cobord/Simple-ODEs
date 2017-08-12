import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

W = np.array([[0,-1],[-1,0]])
theta = np.array([0,0])

def maxZero(x):
    return max(x,0)

vectorizedMaxZero = np.vectorize(maxZero)

# https://arxiv.org/pdf/1512.00897.pdf

def derivX(x, t):
    nonlinearity = np.dot(W,x)+theta
    nonlinearity = vectorizedMaxZero(nonlinearity)
    return -x + nonlinearity
    
ts = np.linspace(0.0, 5.0, 500)
xin = [-1.0, -5.0]

xs = odeint(derivX,xin, ts)

plt.plot(ts,xs[:,0],label='$X_0$')
plt.plot(ts,xs[:,1],label='$X_1$')
plt.legend(loc='best')
plt.savefig('2dThresholdedLinear_time.png')
plt.show()