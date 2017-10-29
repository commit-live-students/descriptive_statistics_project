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
    mode = sale_price.mode()[0]
    #stats = (mean,median,mode)
    plt.hist(sale_price)
    plt.axvline(mean,label='Mean',c='r')
    plt.axvline(median,label='Median',c='y')
    plt.axvline(mode,label='Mode',c='b')
    plt.xlabel('Price')
    plt.ylabel('No of Houses')
    plt.legend()
    #plt.show()
