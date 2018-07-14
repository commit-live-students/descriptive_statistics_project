# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean,median,mode=calculate_statistics()
    result = plt.hist(sale_price, bins=20, color='c', edgecolor='k', alpha=0.65)
    plt.axvline(mean, color='k', linestyle='dashed', linewidth=1)
    # Draw the plot for the mean, median and mode for the dataset
    plt.show()
