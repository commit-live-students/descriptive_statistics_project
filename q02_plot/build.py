# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean, median, mode = sale_price.mean(), sale_price.median(), sale_price.mode()[0]
    plt.figure(figsize=(10, 6))
    plt.hist(sale_price, bins=40)
    plt.axvline(x=mean,label='mean',color='r')
    plt.axvline(x=median,label='median',color='y')
    plt.axvline(x=mode,label='mode',color='b')
    plt.legend()
    plt.show()
#plot()
