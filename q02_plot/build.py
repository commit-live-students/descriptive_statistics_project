# %load q02_plot/build.py
# Default Imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    sales_mean = np.mean(sale_price)
    sales_median = np.median(sale_price)
    sales_mode = sale_price.mode()
   
    plt.figure(figsize=(4, 2))
    plt.hist(sale_price)
    plt.plot(sales_mean, label='mode')
    plt.plot(sales_median, label='median')
    plt.plot(sales_mode, label='mean')
    plt.ylim(0, 10)
    plt.legend()
    plt.show()




