# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']
def plot():
    plt.hist(sale_price.mean())
    plt.hist(sale_price.median())
    plt.hist(sale_price.mode())
    plt.axvline()
    plt.show()
# Draw the plot for the mean, median and mode for the dataset





