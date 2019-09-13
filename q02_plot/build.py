# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.hist(sale_price)
    plt.title("sales price")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.axvline(x = calculate_statistics()[0], linewidth=1, color='r', linestyle='dashed',label='Mean')
    plt.axvline(x = calculate_statistics()[1], linewidth=1, color='g', linestyle='dashed',label='Median')
    plt.axvline(x = calculate_statistics()[2], linewidth=1, color='y', linestyle='dashed',label='Mode')
    plt.show()
