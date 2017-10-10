# %load q02_plot/build.py
# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    a=sale_price.mode()
    plt.hist(sale_price)
    plt.axvline(np.mean(sale_price))
    plt.axvline(np.median(sale_price))
    plt.axvline(a[0])
    plt.show()
# Draw the plot for the mean, median and mode for the dataset
#plot()
