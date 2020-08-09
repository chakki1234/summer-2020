import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

def cal_sim_probability(sample_size, prob):
    #Simulations using Bernoulli r.v.
    data_bern = bernoulli.rvs(size=sample_size,p=prob)
    #Calculating the number of favourable outcomes
    err_ind = np.nonzero(data_bern == 1)
    #calculating the probability
    return np.size(err_ind)/sample_size

def cal_prob(sample_size, event_size):
    return event_size/sample_size
