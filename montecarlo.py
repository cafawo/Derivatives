# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:57:57 2018

@author: Woebbeking
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# See Chapter 2.4
def black_scholes(cpflag,S,K,T,r,sigma):
    # cpflag in {1 for call, -1 for put}
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    price = cpflag * (S * norm.cdf(cpflag*d1, 0.0, 1.0) - K * np.exp(-r * T) * 
            norm.cdf(cpflag*d2, 0.0, 1.0))
    return price

# See Chapter 2.2
def monte_carlo(cpflag,S,K,T,r,sigma,Nsim):
    Z = np.random.normal(0, 1, Nsim)
    S_T = S * np.exp(Z * sigma * np.sqrt(T) + (r-0.5*sigma**2) * T)
    CF_T = np.maximum(cpflag*(S_T - K),0)
    price = np.mean(CF_T) * np.exp(-r*T)
    return price

# Increase Nsim from 1000 to 100000 by 1000
X = range(1000,100000, 1000)
# Compute prices for all Nsim in X
mc_prices = list(map(lambda n: monte_carlo(1,100,100,1,0.01,0.25,n), X))

plt.plot(X,mc_prices)
plt.axhline(y=black_scholes(1,100,100,1,0.01,0.25), color='orange')
plt.xlabel("Number of simulations")
plt.ylabel("Price of the option")
plt.legend(["Monte Carlo", "Black-Scholes"])
plt.show()