# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    mean = sale_price.mean()
    median = sale_price.median()
    mode = sale_price.mode()
    plt.hist(sale_price)
    plt.plot([mean]*1000,range(1000),label = 'Mean')
    plt.plot([median]*1000,range(1000),label = 'Median')
    plt.plot([mode]*1000,range(1000),label = 'Mode')
    plt.ylim(0,1000)
    plt.legend()
    plt.show()
# Draw the plot for the mean, median and mode for the dataset
