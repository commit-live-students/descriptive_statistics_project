# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the datase
def plot():
    mean,median,mode = calculate_statistics()
    plt.figure(figsize=(14,4))
    plt.subplot(131)
    plt.hist(sale_price)
    plt.title('Mean')
    plt.axvline(mean, color='b', linestyle='dashed', linewidth=2)
    plt.subplot(132)
    plt.hist(sale_price)
    plt.title('Median')
    plt.axvline(median, color='b', linestyle='dashed', linewidth=2)
    plt.subplot(133)
    plt.hist(sale_price)
    plt.title('Mode')
    plt.axvline(mode, color='b', linestyle='dashed', linewidth=2)
    plt.show()
