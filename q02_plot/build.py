# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
def plot():
    sale_price = dataframe['SalePrice']
    mean,median,mode=calculate_statistics()
    plt.hist(dataframe['SalePrice'],bins=20,color='c')
    x=sale_price.value_counts()
    d=np.asscalar(x[x.values==x.values.max()].index)
    plt.axvline(mean, color='b', linestyle='dashed', linewidth=2)
    plt.axvline(median, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(d, color='g', linestyle='dashed', linewidth=2)
    plt.show()
