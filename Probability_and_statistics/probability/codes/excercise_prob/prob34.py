import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

prob_E = 3/5
prob_F = 3/10
prob_E_cap_F = 1/5

if(prob_E*prob_F == prob_E_cap_F):
    print('E and F are independent events')
else:
    print('E and F are not independent events')