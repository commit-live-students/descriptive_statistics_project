# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the dataset
def plot():

    mean = sale_price.mean()
    median = sale_price.median()
    mode = np.int64(sale_price.mode())

    plt.hist(sale_price)
    plt.axvline(x=mean, color = 'r')
    plt.show()

    plt.hist(sale_price)
    plt.axvline(x=median, color = 'r')
    plt.show()

    plt.hist(sale_price)
    plt.axvline(x=mode, color = 'r')
    plt.show()
