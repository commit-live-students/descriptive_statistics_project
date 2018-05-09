# %load q02_plot/build.py
# Default Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sales_price = dataframe.loc[:, 'SalePrice']
mode = sales_price.mode()
median = np.median(sales_price)
mean = np.mean(sales_price)

def plot():
    plt.hist(sales_price)
    plt.title('sales price')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.axvline(x = calculate_statistics()[0], linewidth=1, color='r', linestyle='dashed',label='Mean')
    plt.axvline(x = calculate_statistics()[1], linewidth=1, color='g', linestyle='dashed',label='Median')
    plt.axvline(x = calculate_statistics()[2], linewidth=1, color='y', linestyle='dashed',label='Mode')
    plt.show()
# Draw the plot for the mean, median and mode for the dataset


print (plot())









