# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    plt.hist(sale_price,bins=70)
    mean.median.mode = calculate_statistics()
    plt.axvline(mean)
    plt.axvline(median)
    plt.axvline(mode)
    plt.show()


# Draw the plot for the mean, median and mode for the dataset
