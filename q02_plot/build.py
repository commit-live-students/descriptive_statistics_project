# %load q02_plot/build.py
# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']
def plot():
    mode = np.array(sale_price.mode(), dtype=np.int64)
    plt.hist(sale_price)
    plt.axvline(sale_price.mean(),color='r')
    plt.axvline(sale_price.median(),color='g')
    plt.axvline(mode,color='y')
    plt.show()


# Draw the plot for the mean, median and mode for the dataset
