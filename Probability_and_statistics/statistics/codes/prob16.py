import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb
import xlrd 
from functions import *

loc = ("./tables/prob_examp_16/inp.xlsx") 
assumed_index = 4

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

mode = mode(sheet) 
mean = assumed_mean(sheet, assumed_index)
median = median(sheet)

print(mean)
print(median)
print(mode)

