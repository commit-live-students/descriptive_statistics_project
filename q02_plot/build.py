# %load q02_plot/build.py
# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean = sale_price.mean()
    median = sale_price.median()
    mode = sale_price.mode()[0]
    plt.hist(sale_price, bins=40)
    plt.axvline(mode, label='mode',color = 'g')
    plt.axvline(median, label='median' , color = 'r')
    plt.axvline(mean, label='mean',color = 'b')
    plt.show()

plot()


