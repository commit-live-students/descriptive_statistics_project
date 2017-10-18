# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean, median, mode = calculate_statistics()

    plt.axvline(mean, label="Mean", color='g')
    plt.axvline(median, label="Median", color='r')
    plt.axvline(mode, label="Mode", color="y")
    plt.legend()
    plt.show()

    return
