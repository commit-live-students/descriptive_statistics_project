# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    mean = np.mean(sale_price)
    median = np.median(sale_price)
    mode = sale_price.mode()[0]
#     plt.figure(figsize=(10, 6))
    plt.hist(sale_price, bins=10)
    plt.axvline(mean, label='mean', color='r')
    plt.axvline(median, label='median', color='g')
    plt.axvline(mode, label='mode', color='y')
#     plt.ylim(0, 250)
    plt.legend()
    plt.show()
    return
