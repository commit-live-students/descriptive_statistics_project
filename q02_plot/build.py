# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def calculate_statistics(data):
    mean = data.mean()
    median = data.median()
    mode = data.mode().loc[0]
    return (mean, median, mode)
def plot():
    mean, median, mode = calculate_statistics(sale_price)
    ax = sale_price.hist(bins=30)
    ax.axvline(x=mean, color='r', label='Mean')
    ax.axvline(x=median, color='y', label='Median')
    ax.axvline(x=mode, color='g', label='Mode')
    ax.legend()
