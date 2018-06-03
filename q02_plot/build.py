# %load q02_plot/build.py
# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics



dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset

def plot():
    plt.hist(sale_price, bins=40)
    y = np.arange(0,220, 1)
    plt.axvline(x = sale_price.mean())
    plt.axvline(x = sale_price.median())
    plt.axvline(x = sale_price.mode()[0])
    plt.show()



