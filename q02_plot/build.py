# Default Imports
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')


# Draw the plot for the mean, median and mode for the dataset
sale_price = dataframe.loc[:, 'SalePrice']
def plot():
    mean, median, mode = calculate_statistics()
    #print(mean, median, mode)
    plt.hist(sale_price, bins=20)
    plt.axvline(mean, color='r')
    plt.axvline(median, color='g')
    plt.axvline(mode, color='y')
    plt.show()

plot()
