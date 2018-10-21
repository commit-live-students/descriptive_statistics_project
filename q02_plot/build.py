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
    
    mean, median, mod = calculate_statistics()
    x = sale_price
    plt.hist(x, bins=100, color='c', edgecolor='k', alpha=0.65)
    plt.axvline(mean, color='k', linestyle='dashed', linewidth=1)
    plt.axvline(median, color='r', linestyle='dashed', linewidth=1)
    plt.axvline(mod, color='g', linestyle='dashed', linewidth=1)
    plt.show()
plot()


