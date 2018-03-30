# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset

def plot():
    mean, median, mode = calculate_statistics()
    print(mean, median, mode)
    plt.hist(sale_price)
    plt.axvline(mean, color='r')
    plt.axvline(median, c='g')
    plt.axvline(mode, c='y')
    plt.show()

plot()
