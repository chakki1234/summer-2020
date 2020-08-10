import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb
import xlrd 
from functions import *

loc = ("./tables/prob_examp_19/continous_inp.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

median = median(sheet)

print('median -',median)


