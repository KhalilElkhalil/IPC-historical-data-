# -*- coding: utf-8 -*-
"""
Created on Fri May 24 00:51:16 2019

@author: elkhalk
"""

''' impoprt some useful packages ''' 
import pandas as pd
from pandas import Series
from pandas.plotting import lag_plot
import numpy as np
import matplotlib.pyplot as plt
import re
from statsmodels.tsa.ar_model import AR
from statsmodels.graphics.tsaplots import plot_acf
from sklearn.metrics import mean_squared_error

# reading the historical data
df = pd.read_csv('IPC.csv')

# select the price/change % columns 
price_list = []
change_list = []
for i in range(len(df['Price'])):
    price_list.append(float(df['Price'][i].replace(",", "")))
    change_list.append(float(df['Change %'][i][0:-1]))
    
# replace the price/change colums with corresponding lists
df['Price'] = price_list     
df['Change %'] = change_list 

# plot prices with dates 
df.plot(y='Price')
df.plot(y='Change %') 

# histograms 
kwargs = dict(alpha=0.5, bins=100, density=True, stacked=True)
plt.figure(figsize=(9, 3))
plt.subplot(131)
df['Price'].hist(**kwargs)
plt.title('Price')
# plt.hist(df['Price'], **kwargs)
plt.subplot(132)
df['Change %'].hist(**kwargs)
plt.title('Change %')
plt.subplot(133)
# log change histogram 
plt.title('Change log')
df['Change %'].apply(lambda x: np.log(np.abs(x+0.0000000001))).hist(**kwargs)