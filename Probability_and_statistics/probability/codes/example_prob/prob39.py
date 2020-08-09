import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

P = []
X = [0, 1, 2]
mean = temp = 0


sample_size= comb(52, 2)
event_X_is_0 = comb(48, 2) 
event_X_is_1 = comb(48, 1)*comb(4, 1) 
event_X_is_2 = comb(4, 2)

prob_X_is_0 = event_X_is_0/sample_size 
prob_X_is_1 = event_X_is_1/sample_size
prob_X_is_2 = event_X_is_2/sample_size

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

print(err_n_X_is_0,prob_X_is_0)
P.append(prob_X_is_0)

print(err_n_X_is_1,prob_X_is_1)
P.append(prob_X_is_1)

print(err_n_X_is_2,prob_X_is_2)
P.append(prob_X_is_2)

print(P)
for i in range(len(X)):
    mean = mean + X[i]*P[i]

print(mean) 

#To find E(X^2)
for i in range(len(X)):
    temp = temp + X[i]**2*P[i]

#variance 
print(temp - mean**2)
