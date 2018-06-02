# %load q02_plot/build.py
# Default Imports
import pandas as pd

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean, median, mode = calculate_statistics() #sale_price.mean(), sale_price.median(), sale_price.mode()[0]
    plt.hist(sale_price)
    plt.axvline(x=mean, label='mean', color='r')
    plt.axvline(x=median, label='median', color='c')
    plt.axvline(x=mode, label='mode', color='b')
    plt.show()
    



plot()


