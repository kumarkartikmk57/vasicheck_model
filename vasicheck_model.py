import matplotlib.pyplot as plt
import numpy as np

def vmodel(r0,kappa,theta,sigma,T=1,N=1000):

    dt = T/float(N)
    t = np.linspace(0,T,N+1)
    rates = [r0]

    for _ in range(N):
        dr = kappa*(theta-rates[-1])*dt+sigma*np.sqrt(dt)*np.random.normal()
        rates.append(rates[-1]+dr)

    print(rates)
    print(t)
    return t,rates

def plot(t,r):
    plt.plot(t,r)
    plt.show()
vmodel(1.3,0.9,1.5,0.01)
t,r = vmodel(1.3,0.9,1.5,0.01)
plot(t,r)
