import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

#Let X denote the number of aces and be a random variable.
sample_size = 36*36*36
X_is_0 = 30*30*30
X_is_1 = 6*30*30
X_is_2 = 6*6*30
X_is_3 = 6*6*6

prob_X_is_0 = X_is_0/sample_size
prob_X_is_1 = X_is_1/sample_size
prob_X_is_2 = X_is_2/sample_size
prob_X_is_3 = X_is_3/sample_size

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

#For event X_is_3
#Simulations using Bernoulli r.v.
data_bern_X_is_3 = bernoulli.rvs(size=sample_size,p=prob_X_is_3)
#Calculating the number of favourable outcomes
err_ind_X_is_3 = np.nonzero(data_bern_X_is_3 == 1)
#calculating the probability
err_n_X_is_3 = np.size(err_ind_X_is_3)/sample_size
#Theory vs simulation

print(err_n_X_is_0,prob_X_is_0)
print(err_n_X_is_1,prob_X_is_1)
print(err_n_X_is_2,prob_X_is_2)
print(err_n_X_is_3,prob_X_is_3)
