# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
import statistics
import numpy as np

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
 #plt.hist(sale_price)
    plt.hist(sale_price)
    plt.axvline(sale_price.mean(),color='c')
    plt.axvline(sale_price.median(),color='k')
    series1=np.array(sale_price)
    mode1=statistics.mode(series1)
    plt.axvline(mode1,color='k')
    plt.show()

plot()
# Draw the plot for the mean, median and mode for the dataset



