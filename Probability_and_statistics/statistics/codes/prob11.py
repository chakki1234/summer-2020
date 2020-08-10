import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
from math import comb
import xlrd 
from functions import *

loc = ("./tables/prob_examp_11/inp.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
mode = mode(sheet)

print('mode -',mode)