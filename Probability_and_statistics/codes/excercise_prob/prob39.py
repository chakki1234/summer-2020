import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

prob_A = 0.3
prob_B = 0.6

#Since the events A and B are independent
prob_A_cap_B = prob_A*prob_B
print(prob_A_cap_B)

#To find P(A and not B) = P(A) - P(A n B)
print(prob_A - prob_A_cap_B)

#To find P(A or B) 
prob_A_cup_B = prob_A + prob_B - prob_A_cap_B
print(prob_A_cup_B)

#To find P(A u B )' 
print(1- prob_A_cup_B)