import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

sample_size= 2*6
event_A_size = 6
event_B_size = 2
event_A_cap_B_size = 1

prob_A = event_A_size/sample_size
prob_B = event_B_size/sample_size
prob_A_cap_B = event_A_cap_B_size/sample_size

#For event A
#Simulations using Bernoulli r.v.
data_bern_A = bernoulli.rvs(size=sample_size,p=prob_A)
#Calculating the number of favourable outcomes
err_ind_A = np.nonzero(data_bern_A == 1)
#calculating the probability
err_n_A = np.size(err_ind_A)/sample_size

#For event B
#Simulations using Bernoulli r.v.
data_bern_B = bernoulli.rvs(size=sample_size,p=prob_B)
#Calculating the number of favourable outcomes
err_ind_B = np.nonzero(data_bern_B == 1)
#calculating the probability
err_n_B = np.size(err_ind_B)/sample_size

#For event A cap B
#Simulations using Bernoulli r.v.
data_bern_A_cap_B = bernoulli.rvs(size=sample_size,p=prob_A_cap_B)
#Calculating the number of favourable outcomes
err_ind_A_cap_B = np.nonzero(data_bern_A_cap_B == 1)
#calculating the probability
err_n_A_cap_B = np.size(err_ind_A_cap_B)/sample_size
#Theory vs simulation

print(err_n_A,prob_A)
print(err_n_B,prob_B)
print(err_n_A_cap_B,prob_A_cap_B)

if(prob_A*prob_B == prob_A_cap_B):
    print('A and B are independent events')
else:
    print('A and B are not independent events')