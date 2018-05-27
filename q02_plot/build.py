# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    sale_price.sort_values()
    plt.hist(sale_price)
    plt.axvline(x=sale_price.mean(),color='r',label='mean')
    plt.axvline(x=sale_price.median(),color='y',label='median')
    plt.axvline(x=sale_price.mode()[0],color='pink',label='mode')
    plt.legend(loc=0)
    plt.xlabel('Sales Price')
    plt.ylabel('No. of houses')
    plt.show()


