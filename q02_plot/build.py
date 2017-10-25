# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.hist(sale_price)
    plt.axvline(sale_price.mean(), color = 'r', label = 'Mean')
    plt.axvline(sale_price.median(), color = 'g', label = 'Median')
    plt.axvline(sale_price.mode()[0], color = 'y', label = 'Mode')
    plt.xlabel('Prices')
    plt.ylabel('Frequencies')
    plt.title('Price Histogram')
    plt.legend()
    plt.show()
