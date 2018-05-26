# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean = sale_price.mean()
    median = sale_price.median()
    mode = sale_price.mode()[0]
    plt.figure(figsize=(10, 6))
    plt.hist(sale_price, bins=30)
    plt.axvline(x=mean,label='mean',color='r')
    plt.axvline(x=median,label='median',color='g')
    plt.axvline(x=mode,label='mode',color='b')
    #Always label Axes!!
    plt.xlabel('Sales Price')
    plt.ylabel('Number of Houses')
    plt.legend()
plt.show()

