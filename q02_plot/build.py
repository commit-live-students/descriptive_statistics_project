# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    x=calculate_statistics()
    mean=x[0]
    median=x[1]
    mode=x[2]
    plt.hist(sale_price,color='c')
    plt.axvline(mean,linestyle='dashed',color='b',label='mean')
    plt.axvline(median,linestyle='dashed',color='r',label='median')
    plt.axvline(mode[0],linestyle='dashed',color='g',label='mode')
    plt.legend(loc='upper right')
    plt.show()
