import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

sample_size= 2*6
event_A_size = 6
event_B_size = 2
event_A_cap_B_size = 1

prob_A = 1/4
prob_B = 1/2
prob_A_cap_B = 1/8

#To find P(not A and not B) = 1 - P(A U B)
prob_A_cup_B = prob_A + prob_B - prob_A_cap_B

print(1-prob_A_cup_B)