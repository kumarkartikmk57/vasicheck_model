import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

NUM = 1000
POINT = 20

def monte_carlo(x,r0,kappa,theta,sigma,T=1):
    dt = T/float(POINT)
    result = []
    for _ in range(NUM):
        rates = [r0]
        for _ in range(POINT):
            dr = kappa * (theta - rates[-1]) * dt + sigma * np.sqrt(dt) * np.random.normal()
            rates.append(rates[-1] + dr)
        result.append(rates)

    df = pd.DataFrame(result)
    df = df.T
    integral_sum = df.sum() * dt
    present_integral_sim = np.exp(-integral_sum)
    bond = x*np.mean(present_integral_sim)
    print(df)
    print("The bond pris is ",bond)
    return df

def plot(df):
    df.plot()
    plt.show()

df = monte_carlo(100,0.1,0.3,0.1,0.03)
plot(df)

