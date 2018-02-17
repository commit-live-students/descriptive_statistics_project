# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset

def plot():
    plt.hist(sale_price)
    plt.axvline(sale_price.mean(),ls='dashed',c='red')
    plt.axvline(sale_price.median(),ls='dotted',c='cyan')
    plt.axvline(int(sale_price.mode()),ls='dashdot',c='yellow')
    plt.show()
