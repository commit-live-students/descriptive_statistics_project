# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset

def plot():
    plt.hist(sale_price)
    mean=np.mean(sale_price)
    median=np.median(sale_price)
    mode=sale_price.mode()[0]
    plt.axvline(mean,color='r',label='mean')
    plt.axvline(median,color='m',label='median')
    plt.axvline(mode,color='y',label='mode')
    plt.legend()


