# %load q02_plot/build.py
# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

mean1 = np.mean(sale_price)
median1 = np.median(sale_price)
mode1 = pd.Series.mode(sale_price)
mode2 = mode1.values[0]
# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.hist(mean1,median1,mode2)
    plt.show()
    


