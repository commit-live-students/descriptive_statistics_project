# Default Imports
import pandas as pd

import matplotlib.pyplot as plt
plt.switch_backend('agg')
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.hist(sale_price)
    plt.axvline(sale_price.mean(),color='b',linestyle='dashed')
    plt.axvline(sale_price.median(),color='r',linestyle='dashed')
    plt.axvline(sale_price.mode()[0],color='y',linestyle='dashed')
    plt.show()
