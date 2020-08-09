import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

prob_A = 0.3
prob_B = 0.4

#Since events A and B are independent
prob_A_cap_B = prob_A*prob_B
prob_A_cup_B = prob_A + prob_B - prob_A_cap_B
prob_A_given_B = prob_A
prob_B_given_A = prob_B

print(prob_A_cap_B, prob_A_cup_B, prob_A_given_B, prob_B_given_A)

