import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

prob_truth = 3/4
prob_lies = 1/4
prob_of_6 = 1/6
prob_of_not_getting_6 = 5/6

#To find Prob that it is actually six, using Bayes theorem:
print((prob_of_6*prob_truth)/( (prob_of_6*prob_truth) + (prob_of_not_getting_6*prob_lies) ))
