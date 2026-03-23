#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:41:24 2018

@author: Woebbeking
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

#%% Create stock process:
# Random numbers N(0,1)
np.random.seed(888)
Z = np.random.normal(0, 1, 250)
# Initial values for mu and sigma
mu_0 = 0
sigma_0 = .5
def gbm(mu, sigma):
    # returns for our geometric brownian motion
    R = Z * sigma * np.sqrt(1/250) + (mu-0.5*sigma**2) * 1/250
    # stock process (insert 100 for t=0)
    S = np.insert(100*np.exp(np.cumsum(R)), 0, 100)
    return S
    
#%% Generate dynamic graphic:
fig = plt.figure()
ax = fig.add_subplot(111)
# Adjust plotregion with space for sliders
fig.subplots_adjust(left=.1, right=.9, bottom=0.25, top=.9)
# Draw the initial plot
# The 'line' variable is used for modifying the line later
[line] = ax.plot(gbm(mu_0, sigma_0), linewidth=2, color='red')
# Set a fixed y range
plt.xlabel("Time")
plt.ylabel("Price")
ax.set_ylim([25, 175])
# Add a slider for mu
mu_slider_ax  = fig.add_axes([0.1, 0.1, 0.8, 0.03], facecolor='white')
mu_slider = Slider(mu_slider_ax, 'Mu', -.5, .5, valinit=mu_0)
# Add a slider for sigma
sigma_slider_ax = fig.add_axes([0.1, 0.05, 0.8, 0.03], facecolor='white')
sigma_slider = Slider(sigma_slider_ax, 'Sigma', 0, 1, valinit=sigma_0)
# Define an action for modifying the line when a slider's value is changed
def sliders_on_changed(val):
    line.set_ydata(gbm(mu_slider.val, sigma_slider.val))
    fig.canvas.draw_idle()
# Monitor sliders and show plot
mu_slider.on_changed(sliders_on_changed)
sigma_slider.on_changed(sliders_on_changed)
plt.show()
