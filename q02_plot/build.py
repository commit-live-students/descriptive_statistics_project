# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def calculate_statistics():
    return sale_price.mean(), sale_price.median(), sale_price.mode().values[0]



def plot():
    mean, median, mode = calculate_statistics()
    plt.hist(sale_price, color='c')
    plt.axvline(mean, color='b', linestyle='dashed', linewidth=2)
    plt.axvline(median, color='b', linestyle='dashed', linewidth=2)
    plt.axvline(pd.Series(mode).values, color='b', linestyle='dashed', linewidth=2)
    
# Draw the plot for the mean, median and mode for the dataset

plot()




