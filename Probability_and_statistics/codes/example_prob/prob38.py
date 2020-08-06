import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

P = []
X = [1, 2, 3, 4, 5, 6]
mean = temp = 0


sample_size= 6
event_X_is_1 = 1 
event_X_is_2 = 1 
event_X_is_3 = 1
event_X_is_4 = 1
event_X_is_5 = 1
event_X_is_6 = 1

prob_X_is_1 = event_X_is_1/sample_size
prob_X_is_2 = event_X_is_2/sample_size
prob_X_is_3 = event_X_is_3/sample_size
prob_X_is_4 = event_X_is_4/sample_size
prob_X_is_5 = event_X_is_5/sample_size
prob_X_is_6 = event_X_is_6/sample_size

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

#For event X_is_3
#Simulations using Bernoulli r.v.
data_bern_X_is_3 = bernoulli.rvs(size=sample_size,p=prob_X_is_3)
#Calculating the number of favourable outcomes
err_ind_X_is_3 = np.nonzero(data_bern_X_is_3 == 1)
#calculating the probability
err_n_X_is_3 = np.size(err_ind_X_is_3)/sample_size

#For event X_is_4
#Simulations using Bernoulli r.v.
data_bern_X_is_4 = bernoulli.rvs(size=sample_size,p=prob_X_is_4)
#Calculating the number of favourable outcomes
err_ind_X_is_4 = np.nonzero(data_bern_X_is_4 == 1)
#calculating the probability
err_n_X_is_4 = np.size(err_ind_X_is_4)/sample_size
#Theory vs simulation

#For event X_is_5
#Simulations using Bernoulli r.v.
data_bern_X_is_5 = bernoulli.rvs(size=sample_size,p=prob_X_is_5)
#Calculating the number of favourable outcomes
err_ind_X_is_5 = np.nonzero(data_bern_X_is_5 == 1)
#calculating the probability
err_n_X_is_5 = np.size(err_ind_X_is_5)/sample_size
#Theory vs simulation

#For event X_is_6
#Simulations using Bernoulli r.v.
data_bern_X_is_6 = bernoulli.rvs(size=sample_size,p=prob_X_is_6)
#Calculating the number of favourable outcomes
err_ind_X_is_6 = np.nonzero(data_bern_X_is_6 == 1)
#calculating the probability
err_n_X_is_6 = np.size(err_ind_X_is_6)/sample_size
#Theory vs simulation

print(err_n_X_is_1,prob_X_is_1)
P.append(prob_X_is_1)

print(err_n_X_is_2,prob_X_is_2)
P.append(prob_X_is_2)

print(err_n_X_is_3,prob_X_is_3)
P.append(prob_X_is_3)

print(err_n_X_is_4,prob_X_is_4)
P.append(prob_X_is_4)

print(err_n_X_is_5,prob_X_is_5)
P.append(prob_X_is_5)

print(err_n_X_is_6,prob_X_is_6)
P.append(prob_X_is_6)

print(P)
for i in range(len(X)):
    mean = mean + X[i]*P[i]

print(mean) 

#To find E(X^2)
for i in range(len(X)):
    temp = temp + X[i]**2*P[i]

#variance 
print(temp - mean**2)
