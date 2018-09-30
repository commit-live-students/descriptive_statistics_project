# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.figure()
    sale_price.hist(bins=40)
    plt.axvline(x=sale_price.mean(),label='mean')
    plt.axvline(x=sale_price.median(),label='median')
    plt.axvline(x=np.array(sale_price.mode())[0],label='mode')
    plt.legend()
    plt.show();

plot()


