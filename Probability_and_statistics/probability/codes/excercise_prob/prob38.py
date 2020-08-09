import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

prob_A = 1/2
prob_B = 7/12
prob_A_cap_B_complement = 1/4

#To find if the events are independent or not
prob_A_cap_B = 1 - prob_A_cap_B_complement

if(prob_A*prob_B == prob_A_cap_B):
    print('A and B are independent events')
else:
    print('A and B are not independent events')

