# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean=sale_price.mean()
    median=sale_price.median()
    mode_series=sale_price.mode()
    mode=mode_series[0]

    plt.hist(sale_price,bins=100)
    plt.axvline(mean,color='green',label='Mean')
    plt.axvline(median,color='red',label='Median')
    plt.axvline(mode,color='blue',label='Mode')
    plt.legend()
    plt.show()
