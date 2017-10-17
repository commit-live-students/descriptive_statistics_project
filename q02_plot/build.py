# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']
def plot():

    plt.hist(sale_price, bins = 50)
    plt.axvline(sale_price.mean(), color='y', linestyle='dashed', linewidth=2)
    plt.axvline(sale_price.median(), color='b', linestyle='dashed', linewidth=2)
    plt.axvline(sale_price.mode().values[0], color='g', linestyle='dashed', linewidth=2)
    plt.show()




# Draw the plot for the mean, median and mode for the dataset
