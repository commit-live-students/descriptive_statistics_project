# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.figure(figsize=(10, 6))
    plt.hist(sale_price, bins=40)
    plt.axvline(calculate_statistics()[0],label='mean',color='Red')
    plt.axvline(calculate_statistics()[1],label='median',color='Green')
    plt.axvline(calculate_statistics()[2],label='mode',color='Yellow')
    plt.legend()
    plt.show()
    return
