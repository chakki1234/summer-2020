import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

P = []
X = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mean = 0

sample_size= 36
event_X_is_2 = 1 
event_X_is_3 = 2
event_X_is_4 = 3
event_X_is_5 = 4
event_X_is_6 = 5
event_X_is_7 = 6
event_X_is_8 = 5
event_X_is_9 = 4
event_X_is_10 = 3
event_X_is_11 = 2
event_X_is_12 = 1

prob_X_is_2 = event_X_is_2/sample_size
prob_X_is_3 = event_X_is_3/sample_size
prob_X_is_4 = event_X_is_4/sample_size
prob_X_is_5 = event_X_is_5/sample_size
prob_X_is_6 = event_X_is_6/sample_size
prob_X_is_7 = event_X_is_7/sample_size
prob_X_is_8 = event_X_is_8/sample_size
prob_X_is_9 = event_X_is_9/sample_size
prob_X_is_10 = event_X_is_10/sample_size
prob_X_is_11 = event_X_is_11/sample_size
prob_X_is_12 = event_X_is_12/sample_size

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

#For event X_is_7
#Simulations using Bernoulli r.v.
data_bern_X_is_7 = bernoulli.rvs(size=sample_size,p=prob_X_is_7)
#Calculating the number of favourable outcomes
err_ind_X_is_7 = np.nonzero(data_bern_X_is_7 == 1)
#calculating the probability
err_n_X_is_7 = np.size(err_ind_X_is_7)/sample_size
#Theory vs simulation

#For event X_is_8
#Simulations using Bernoulli r.v.
data_bern_X_is_8 = bernoulli.rvs(size=sample_size,p=prob_X_is_8)
#Calculating the number of favourable outcomes
err_ind_X_is_8 = np.nonzero(data_bern_X_is_8 == 1)
#calculating the probability
err_n_X_is_8 = np.size(err_ind_X_is_8)/sample_size
#Theory vs simulation

#For event X_is_9
#Simulations using Bernoulli r.v.
data_bern_X_is_9 = bernoulli.rvs(size=sample_size,p=prob_X_is_9)
#Calculating the number of favourable outcomes
err_ind_X_is_9 = np.nonzero(data_bern_X_is_9 == 1)
#calculating the probability
err_n_X_is_9 = np.size(err_ind_X_is_9)/sample_size
#Theory vs simulation

#For event X_is_10
#Simulations using Bernoulli r.v.
data_bern_X_is_10 = bernoulli.rvs(size=sample_size,p=prob_X_is_10)
#Calculating the number of favourable outcomes
err_ind_X_is_10 = np.nonzero(data_bern_X_is_10 == 1)
#calculating the probability
err_n_X_is_10 = np.size(err_ind_X_is_10)/sample_size
#Theory vs simulation

#For event X_is_11
#Simulations using Bernoulli r.v.
data_bern_X_is_11 = bernoulli.rvs(size=sample_size,p=prob_X_is_11)
#Calculating the number of favourable outcomes
err_ind_X_is_11 = np.nonzero(data_bern_X_is_11 == 1)
#calculating the probability
err_n_X_is_11 = np.size(err_ind_X_is_11)/sample_size
#Theory vs simulation

#For event X_is_12
#Simulations using Bernoulli r.v.
data_bern_X_is_12 = bernoulli.rvs(size=sample_size,p=prob_X_is_12)
#Calculating the number of favourable outcomes
err_ind_X_is_12 = np.nonzero(data_bern_X_is_12 == 1)
#calculating the probability
err_n_X_is_12 = np.size(err_ind_X_is_12)/sample_size
#Theory vs simulation


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

print(err_n_X_is_7,prob_X_is_7)
P.append(prob_X_is_7)

print(err_n_X_is_8,prob_X_is_8)
P.append(prob_X_is_8)

print(err_n_X_is_9,prob_X_is_9)
P.append(prob_X_is_9)

print(err_n_X_is_10,prob_X_is_10)
P.append(prob_X_is_10)

print(err_n_X_is_11,prob_X_is_11)
P.append(prob_X_is_11)

print(err_n_X_is_12,prob_X_is_12)
P.append(prob_X_is_12)


for i in range(len(X)):
    mean = mean + X[i]*P[i]

print(mean)