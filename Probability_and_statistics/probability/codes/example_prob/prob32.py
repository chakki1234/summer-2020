import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

X = []

def cal_value_of_x(heads, tails):
    return heads*2 - tails*1.5

def append_X(number):
    if number in X:
        pass
    else:
        X.append(number)


#values the random variable can take

#for HHH:
append_X(cal_value_of_x(3,0))

#for HHT:
append_X(cal_value_of_x(2,1))

#for HTH:
append_X(cal_value_of_x(2,1))

#for THH:
append_X(cal_value_of_x(2,1))

#for TTH:
append_X(cal_value_of_x(1,2))

#for THT:
append_X(cal_value_of_x(1,2))

#for HTT:
append_X(cal_value_of_x(1,2))

#for TTT:
append_X(cal_value_of_x(0,3))

print(X)