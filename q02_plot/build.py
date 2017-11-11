# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
        mean = sale_price.mean()
        median = sale_price.median()
        mode= sale_price.mode()
        sale_price.plot(kind='hist')
        plt.axvline(mean,color='b', linestyle='dashed', linewidth=2)
        plt.axvline(median,color='g', linestyle='dashed', linewidth=2)
        plt.axvline(mode[0],color='b', linestyle='dashed', linewidth=2)
        plt.show()
        return
