import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

prob_X_is_0 = 0.1

#Sum of probabilities is equal to 1
# prob_X_is_0 + prob_X_is_1 + prob_X_is_2 + prob_X_is_3 + prob_X_is_4 = 1
k = 0.9/6

prob_X_is_1 = k 
prob_X_is_2 = 2*k
prob_X_is_3 = 2*k
prob_X_is_4 = k


#P(X>=2)
print(prob_X_is_2 + prob_X_is_3 + prob_X_is_4)

#P(X=2)
print(prob_X_is_2)

#P(X<=2)
print(prob_X_is_0 + prob_X_is_1 + prob_X_is_2)