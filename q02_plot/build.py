# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    value=calculate_statistics()
    #print(value[0])
    plt.hist(sale_price)
    plt.axvline(value[0])
    plt.axvline(value[1])
    plt.axvline(value[2])
    plt.show()
