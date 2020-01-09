# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.figure()
    plt.hist(Sales_price, bins=60)
    plt.axvline(sale_price.mean(),color='r',linewidth=4)
    plt.axvline(sale_price.median(),color='g',linewidth=4)
    plt.axvline(sale_price.mode(),color='b',linewidth=4)
    plt.show()
    
    


