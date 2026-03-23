# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:31:05 2018

@author: Woebbeking
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

#%% Black-Scholes formula
def black_scholes(cpflag,S,K,T,r,sigma):
    # cpflag in {1 for call, -1 for put}
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    price = cpflag * (S * norm.cdf(cpflag*d1, 0.0, 1.0) - K * np.exp(-r * T) * 
            norm.cdf(cpflag*d2, 0.0, 1.0))
    return price


#%% Generate dynamic graphic:
# Initial parameters
K_0,T_0,r_0,sigma_0 = 50, 1, 0.05, 0.2
X = np.linspace(1,100,100)
fig = plt.figure()
ax = fig.add_subplot(111)
# Adjust plotregion with space for sliders
fig.subplots_adjust(left=.1, right=.9, bottom=0.3, top=.9)
# Draw the initial plot
plt.plot(X,np.maximum(X-K_0,0), '--')
plt.plot(X,black_scholes(1,X,K_0,T_0,r_0,sigma_0))
# The 'line' variable is used for modifying the line later
[line] = ax.plot(X, black_scholes(1,X,K_0,T_0,r_0,sigma_0), linewidth=2)
plt.xlabel("Price of the underlying at t")
plt.ylabel("Value of the option")
plt.legend(["Intrinsic value", "Option 1", "Option 2"])
#ax.set_ylim([25, 175])
# Add slider for option parameter
T_slider_ax  = fig.add_axes([0.1, 0.15, 0.8, 0.03], facecolor='white')
T_slider = Slider(T_slider_ax, 'Time', 0.01, 4, valinit=T_0)
r_slider_ax  = fig.add_axes([0.1, 0.1, 0.8, 0.03], facecolor='white')
r_slider = Slider(r_slider_ax, 'Rate', 0, 0.2, valinit=r_0)
sigma_slider_ax = fig.add_axes([0.1, 0.05, 0.8, 0.03], facecolor='white')
sigma_slider = Slider(sigma_slider_ax, 'Vola', 0.01, .78, valinit=sigma_0)
# Define an action for modifying the line when a slider's value is changed
def sliders_on_changed(val):
    line.set_ydata(
            black_scholes(1,X,K_0,
                          T_slider.val,
                          r_slider.val,
                          sigma_slider.val))
    fig.canvas.draw_idle()
# Monitor sliders and show plot
T_slider.on_changed(sliders_on_changed)
r_slider.on_changed(sliders_on_changed)
sigma_slider.on_changed(sliders_on_changed)
plt.show()
