# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']
mean,median,mode=calculate_statistics()

# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.figure(figsize=(10, 6))
    plt.hist(sale_price, bins=40)
    plt.axvline(x=mean, linewidth=3, color='r',label='mean')
    plt.axvline(x=median, linewidth=3, color='y',label='median')
    plt.axvline(x=mode, linewidth=3, color='m',label='mode')
    plt.legend()
    plt.show()



