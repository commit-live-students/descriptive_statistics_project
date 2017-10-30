# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    plt.hist(sale_price)
    plt.axvline(x=sale_price.mean(),color='red')
    plt.axvline(x=sale_price.median(),color='k')
    plt.axvline(x=sale_price.mode()[0],color='y')
    plt.show()
# Draw the plot for the mean, median and mode for the dataset
