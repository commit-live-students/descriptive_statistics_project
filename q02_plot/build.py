# %load q02_plot/build.py
# Default Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset

def plot():
    mean = np.mean(sale_price)
    median = np.median(sale_price)
    mode = sale_price.mode()
    plt.figure(figsize=(10,6))
    plt.hist(sale_price, bins=40)
   
 
    plt.show()
plot()


