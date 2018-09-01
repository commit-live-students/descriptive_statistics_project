# %load q02_plot/build.py
# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as s
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']



# Draw the plot for the mean, median and mode for the dataset
def plot():
    ''' Function which plots the histogram and comparing the 3 Ms'''
    mean = np.mean(sale_price)
    mode = s.mode(sale_price)
    median = np.median(sale_price)
    plt.hist(sale_price)
    plt.plot([mean]*800,np.arange(0,800),label='mean')
    plt.plot([median]*800,np.arange(0,800),label='median')
    plt.plot([mode]*800,np.arange(0,800),label='mode')
    plt.legend()
    plt.show()

plot()



