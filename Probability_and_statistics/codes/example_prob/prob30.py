import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

prob_T1 = 3/10
prob_T2 = 1/5
prob_T3 = 1/10
prob_T4 = 2/5
prob_L_given_T1 = 1/4
prob_L_given_T2 = 1/3
prob_L_given_T3 = 1/12
prob_L_given_T4 = 0

#To find P(T1|L), using Bayes theorem:
prob_T1_given_L = (prob_T1*prob_L_given_T1)/( (prob_T1*prob_L_given_T1) + (prob_T2*prob_L_given_T2) + (prob_T3*prob_L_given_T3) + (prob_T4*prob_L_given_T4))
print(prob_T1_given_L)