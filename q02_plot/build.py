# %load q02_plot/build.py
# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    mean=np.mean(sale_price)
    median=np.median(sale_price)
    mode=sale_price.mode()[0]
    plt.axvline(x=mean)
    plt.axvline(x=median)
    plt.axvline(x=mode)
    plt.show()


plot()


