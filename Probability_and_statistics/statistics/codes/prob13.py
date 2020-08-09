import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb
import xlrd 
from functions import *

loc = ("./tables/prob_examp_13/inp.xlsx") 
assumed_index = 5

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

mode = mode(sheet) 
mean = assumed_mean(sheet, assumed_index)


print(mode)
print(mean)
