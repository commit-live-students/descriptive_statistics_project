# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean, median, mode = calculate_statistics()
    plt.hist(sale_price, bins = 60, color = 'c')
    plt.axvline(mean, color = 'b', linestyle = 'dashed', linewidth = 2)
    plt.axvline(median, color = 'b', linestyle = 'dashed', linewidth = 2)
    plt.axvline(pd.Series(mode).values, color = 'b', linestyle = 'dashed', linewidth = 2)


