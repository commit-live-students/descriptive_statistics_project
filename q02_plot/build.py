# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    sale_price.hist(bins=50)
    mean,median, mode = calculate_statistics()
    plt.axvline(x=mean,color='red')
    plt.axvline(x=median,color='black')
    plt.axvline(x=mode,color='yellow')
    plt.show()
