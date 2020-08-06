import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

#Let X denote the number of aces and be a random variable.
sample_size = 52*52 
X_is_0 = 48*48 
X_is_1 = 4*48*2
X_is_2 = 4*4

prob_X_is_0 = X_is_0/sample_size
prob_X_is_1 = X_is_1/sample_size
prob_X_is_2 = X_is_2/sample_size

#For event X_is_0
#Simulations using Bernoulli r.v.
data_bern_X_is_0 = bernoulli.rvs(size=sample_size,p=prob_X_is_0)
#Calculating the number of favourable outcomes
err_ind_X_is_0 = np.nonzero(data_bern_X_is_0 == 1)
#calculating the probability
err_n_X_is_0 = np.size(err_ind_X_is_0)/sample_size

#For event X_is_1
#Simulations using Bernoulli r.v.
data_bern_X_is_1 = bernoulli.rvs(size=sample_size,p=prob_X_is_1)
#Calculating the number of favourable outcomes
err_ind_X_is_1 = np.nonzero(data_bern_X_is_1 == 1)
#calculating the probability
err_n_X_is_1 = np.size(err_ind_X_is_1)/sample_size

#For event X_is_2
#Simulations using Bernoulli r.v.
data_bern_X_is_2 = bernoulli.rvs(size=sample_size,p=prob_X_is_2)
#Calculating the number of favourable outcomes
err_ind_X_is_2 = np.nonzero(data_bern_X_is_2 == 1)
#calculating the probability
err_n_X_is_2 = np.size(err_ind_X_is_2)/sample_size
#Theory vs simulation

print(err_n_X_is_0,prob_X_is_0)
print(err_n_X_is_1,prob_X_is_1)
print(err_n_X_is_2,prob_X_is_2)

