# %load q02_plot/build.py
# Default Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset

def plot():
    plt.hist(sale_price,bins=60)
    plt.axvline(x=sale_price.mean(), color='b',linewidth=2,label='Mean')
    plt.axvline(x=sale_price.median(), color='g',linewidth=2, label='Median')
    plt.axvline(x=np.array(sale_price.mode(), dtype=np.int64)[0], color='r',linewidth=2, label='Mode')
    plt.legend()
    plt.show()
    


