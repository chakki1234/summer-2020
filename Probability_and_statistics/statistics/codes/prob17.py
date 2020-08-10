import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb
import xlrd 
from functions import *

loc = ("./tables/prob_examp_17/inp.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

# from the given info l = 20, n = 60, cf = 5 + x, f = 20, h=10, median = 28.5 using the median formula
l = 20
n = 60
f = 20
h = 10
median = 28.5 
cf  = -((median - l)*f/h - n/2)
x = cf - 5

y = n - to_get_numbers(sheet) - x

print('x-', x)
print('y-', y)

