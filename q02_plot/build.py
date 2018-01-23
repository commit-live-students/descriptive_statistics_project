# Default Imports
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
import pandas as pd

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean, median, mode = calculate_statistics()
    plt.hist(sale_price, color='c')
    plt.axvline(mean, color='b', linestyle='dashed', linewidth=2)
    plt.axvline(median, color='b', linestyle='dashed', linewidth=2)
    plt.axvline(pd.Series(mode).values, color='b', linestyle='dashed', linewidth=2)

