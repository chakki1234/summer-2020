import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb

def mean(sheet):
    f = [sheet.cell_value(i, 1) for i in range(1, sheet.nrows)]
    x = [ np.sum(np.fromstring(sheet.cell_value(j, 0) , dtype=int, sep='-')) / 2 for j in range(1, sheet.nrows)]
    fx = np.array(f)*np.array(x)
    
    return np.sum(fx)/np.sum(f)

def mode(sheet):
    frequency = [sheet.cell_value(i, 1) for i in range(1, sheet.nrows)]
    f1 = max(frequency)
    f0 = frequency[frequency.index(max(frequency))-1]
    f2 = frequency[frequency.index(max(frequency))+1] 
    modal_class = np.fromstring( sheet.cell_value( frequency.index(max(frequency))+1 , 0) , dtype=int, sep='-')
    h = modal_class[1] - modal_class[0]
    l = modal_class[0]
    
    return l + (f1-f0)/(2*f1-f0-f2)*h

def assumed_mean(sheet, assumed_index):
    f = np.array([sheet.cell_value(i, 1) for i in range(1, sheet.nrows)])
    x = np.array([np.sum(np.fromstring(sheet.cell_value(j, 0) , dtype=int, sep='-')) / 2 for j in range(1, sheet.nrows)])
    x_a = x - x[assumed_index-1]
    class_limits = np.fromstring( sheet.cell_value(1 , 0) , dtype=int, sep='-')
    h = class_limits[1] - class_limits[0]
    u = x_a / h
    fu = f * u
   
    return x[assumed_index-1] + h * np.sum(fu)/np.sum(f)

def median(sheet):
    f = np.array([sheet.cell_value(i, 1) for i in range(1, sheet.nrows)])
    cf = np.array([np.sum(f[0:j+1]) for j in range(0, len(f))])
    
    n_by_2 = np.sum(f)/2
    filter_cf = cf[cf >= n_by_2]
    index, = np.where(cf == filter_cf[0])
    index = index[0]
    
    class_limits = np.fromstring( sheet.cell_value(index+1 , 0) , dtype=int, sep='-')
    l = class_limits[0]
    h = class_limits[1] - class_limits[0]
    
    return l + (n_by_2 - cf[index-1])*h/f[index] 


#########################################################

# def mean2(sheet):
#     f=0
#     fx = 0
    
#     for i in range(1, sheet.nrows):
# 	    f= f + sheet.cell_value(i, 1)
	
#     for j in range(1, sheet.nrows):
# 	    fx = fx + sheet.cell_value(j, 3)
    
#     return fx/f

# def assumed_mean2(sheet, assumed_index):
#     f=0
#     fiui = 0
    
#     for i in range(1, sheet.nrows):
# 	    f= f + sheet.cell_value(i, 1)
	
#     for j in range(1, sheet.nrows):
# 	    fiui = fiui + sheet.cell_value(j, 5)
    
#     a = sheet.cell_value(assumed_index, 2)
#     class_limits = np.fromstring( sheet.cell_value(1 , 0) , dtype=int, sep='-')
#     h = class_limits[1] - class_limits[0]

#     return a + h * fiui/f 
