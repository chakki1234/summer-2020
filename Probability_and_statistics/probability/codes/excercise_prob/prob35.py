import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb



prob_A = 1/2
prob_A_cup_B = 3/5

# To find P if the events are mutually exclusive 
prob_B = prob_A_cup_B - prob_A 
print(prob_B)

# To find P if the events are independent 
prob_B = 2*(prob_A_cup_B - prob_A)
print(prob_B)
