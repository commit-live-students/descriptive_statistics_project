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
    sale_price.plot.hist(grid=True, bins=20, rwidth=0.9, color='#607c8e')
    plt.axvline(x=sale_price.mean(), color='k', linestyle='dashed', linewidth=1)
    plt.axvline(x=sale_price.median(), color='k', linestyle='dashed', linewidth=1)
    plt.axvline(x=sale_price.mode()[0], color='k', linestyle='dashed', linewidth=1)
plot()


