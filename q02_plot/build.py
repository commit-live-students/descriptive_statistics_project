# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.hist(Sales_price, bins=20, color='c')
    plt.axvline(x=Sales_price.mean(), color='b', linestyle='dashed', linewidth=2)
    plt.axvline(x=Sales_price.median(), color='red', linestyle='dashed', linewidth=2)
    plt.axvline(x=Sales_price.mode()[0], color='r', linestyle='dashed', linewidth=2)
    return plt.show()
    
