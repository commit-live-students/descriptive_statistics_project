# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the dataset
def plot() :
    mean=sale_price.mean()
    median=sale_price.median()
    mode_series=sale_price.mode()
    mode=mode_series[0]

    plt.hist(sale_price,bins=100,color='y')
    plt.axvline(mean,color='red',label='Mean')
    plt.axvline(median,color='blue',label='Median')
    plt.axvline(mode,color='green',label='Mode')
    plt.xlabel('sale Price')
    plt.legend()
    plt.show()
