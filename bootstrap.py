# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:26:45 2018

@author: Woebbeking
"""

import numpy as np

# Bootstrapping for swap rates (assuming annual payments)
def swap_bootstrap(swap_rates):
    discount_factors = []
    for s in swap_rates:
        # See Slide 61 
        DF_T = (1 - s * sum(discount_factors)) / (1 + s)
        discount_factors.append(DF_T)
        
    zero_rates = []
    for T, DF_T in enumerate(discount_factors):
        # Python starts counting at 0, hence, +1
        T = T + 1
        # See Slide 48
        r_T = (1 / DF_T) ** (1 / T) - 1
        zero_rates.append(round(r_T,4))
        
    return [discount_factors, zero_rates]

print(swap_bootstrap([0.04, 0.05, 0.06]))

def swap_pricing(discount_factors):
    s_T = (1 - discount_factors[-1]) / sum(discount_factors)
    return round(s_T, 2)
    
discount_factors = swap_bootstrap([0.04, 0.05, 0.06])[0]
print(swap_pricing(discount_factors))

