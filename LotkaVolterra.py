import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

time=np.linspace(0,15,5*1024)

def derivN(N, t):
    """Return the derivative of the vector N, which represents
    the tuple (N1, N2). """

    N1, N2  = N
    return np.array([N1*(1 - N1 - .7*N2), N2*(1 - N2 - .3*N1)])

def coupled(time, init, ax):
    """Visualize the system of coupled equations, by passing a timerange and
    initial conditions for the coupled equations.

    The initical condition is the value that (N1, N2) will assume at the first
    timestep. """

    N = integrate.odeint(derivN, init, time)
    ax[0].plot(N[:,0], N[:,1], label='[{:.1f}, {:.1f}]'.format(*init))  # plots N2 vs N1, with time as an implicit parameter
    l1, = ax[1].plot(time, N[:,0], label='[{:.1f}, {:.1f}]'.format(*init))
    ax[1].plot(time, N[:,1], color=l1.get_color())
    
fh, ax = plt.subplots(1,2)
coupled(time, [.3, 1/.7], ax)
coupled(time, [.4, 1/.7], ax)
coupled(time, [1/.7, .3], ax)
coupled(time, [.5, .5], ax)
coupled(time, [.1, .1], ax)
ax[0].legend()
ax[1].legend()
ax[0].set_xlabel('N1')
ax[0].set_ylabel('N2')
ax[1].set_xlabel('time')
ax[1].set_ylabel(r'$N_i$')
ax[0].set_title('implicit')
ax[1].set_title('explicit (i.e. vs independant variable time)')
plt.show()