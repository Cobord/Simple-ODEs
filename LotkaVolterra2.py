import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

time=np.linspace(0,15,5*1024)
epsilon = [0,0]
aij = [[0,.1],[-.1,0]]

def deriv(currentQs,currentPs,dof,t):
    Pdot=epsilon
    Qdot=np.zeros(dof)
    tempVar1 = np.dot(aij,currentQs)
    for l in range(dof):
        tempVar2=np.exp(currentPs[l]+.5*tempVar1[l])
        Pdot-=tempVar2*.5*aij[l,:]
        Qdot+=tempVar2
    return [Qdot,Pdot]