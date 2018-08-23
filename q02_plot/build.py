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
    mean = sale_price.mean()
    median = sale_price.median()
    mode = sale_price.mode()
    plt.hist(sale_price)
    plt.plot([mean,mean,mean],[1,5,sale_price.mean()],'r')
    plt.plot([median,median,median],[1,5,sale_price.mean()],'r')
    plt.plot([mode,mode,mode],[1,5,sale_price.mean()],'r')
    plt.show()
# Draw the plot for the mean, median and mode for the dataset


#plt.boxplot(sale_price)
plot()
#plt.show()
plot()

