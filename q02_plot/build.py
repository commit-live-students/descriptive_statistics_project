# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
import numpy as np
plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the dataset
def plot():
    data = [(sale_price.mean()),(sale_price.median()),(sale_price.mode())]
    plt.hist(data, bins=7)
    plt.axvline()
plot()



