# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    mean = sale_price.mean()
    median = sale_price.median()
    mode_temp = sale_price.mode()
    mode = mode_temp.item()
    plt.hist(sale_price)
    plt.axvline(mean)
    plt.show()
    plt.hist(sale_price)
    plt.axvline(median)
    plt.show()
    plt.hist(sale_price)
    plt.axvline(mode)
    plt.show()
    
# Draw the plot for the mean, median and mode for the dataset
