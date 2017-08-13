<<<<<<< HEAD
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def LotkaVolterra(state,t):
  x = state[0]
  y = state[1]
  alpha = 0.1
  beta =  0.1
  sigma = 0.1
  gamma = 0.1
  xd = x*(alpha - beta*y)
  yd = -y*(gamma - sigma*x)
  return [xd,yd]

t = np.arange(0,500,1)
state0 = [0.5,0.5]
state = odeint(LotkaVolterra,state0,t)
plt.figure()
plt.plot(t,state)
plt.ylim((0,8))
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.legend(('x (prey)','y (predator)'))
plt.title('Lotka-Volterra equations')

# animation in state-space
plt.figure()
pb, = plt.plot(state[:,0],state[:,1],'b-',alpha=0.2)
plt.xlabel('x (prey population size)')
plt.ylabel('y (predator population size)')
p, = plt.plot(state[0:10,0],state[0:10,1],'b-')
pp, = plt.plot(state[10,0],state[10,1],'b.',markersize=10)
tt = plt.title("%4.2f sec" % 0.00)

# animate
step=2
for i in np.arange(1,len(state)-21,step):
  p.set_xdata(state[10+i:20+i,0])
  p.set_ydata(state[10+i:20+i,1])
  pp.set_xdata(state[19+i,0])
  pp.set_ydata(state[19+i,1])
  tt.set_text("%d steps" % (i))
=======
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def LotkaVolterra(state,t):
  x = state[0]
  y = state[1]
  alpha = 0.1
  beta =  0.1
  sigma = 0.1
  gamma = 0.1
  xd = x*(alpha - beta*y)
  yd = -y*(gamma - sigma*x)
  return [xd,yd]

t = np.arange(0,500,1)
state0 = [0.5,0.5]
state = odeint(LotkaVolterra,state0,t)
plt.figure()
plt.plot(t,state)
plt.ylim((0,8))
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.legend(('x (prey)','y (predator)'))
plt.title('Lotka-Volterra equations')

# animation in state-space
plt.figure()
pb, = plt.plot(state[:,0],state[:,1],'b-',alpha=0.2)
plt.xlabel('x (prey population size)')
plt.ylabel('y (predator population size)')
p, = plt.plot(state[0:10,0],state[0:10,1],'b-')
pp, = plt.plot(state[10,0],state[10,1],'b.',markersize=10)
tt = plt.title("%4.2f sec" % 0.00)

# animate
step=2
for i in np.arange(1,len(state)-21,step):
  p.set_xdata(state[10+i:20+i,0])
  p.set_ydata(state[10+i:20+i,1])
  pp.set_xdata(state[19+i,0])
  pp.set_ydata(state[19+i,1])
  tt.set_text("%d steps" % (i))
>>>>>>> 2cbb52159d861de959f7416e03ec8c260988f889
  plt.draw()