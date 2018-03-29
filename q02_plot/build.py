# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean =  np.mean(sale_price)
    median = np.median(sale_price)
    mode =  sale_price.value_counts(ascending=False).index[0]

    plt.hist(sale_price)
    plt.axvline(x=mean,color='b', linestyle='dashed')
    plt.show()

    plt.hist(sale_price)
    plt.axvline(x=median,color='b', linestyle='dashed')
    plt.show()

    plt.hist(sale_price)
    plt.axvline(x=mode,color='b', linestyle='dashed')
    plt.show()
