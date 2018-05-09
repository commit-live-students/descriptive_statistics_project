# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    mean,median,mode = calculate_statistics()
    plt.hist(sale_price,color='green',alpha=0.5,bins=200)
    plt.axvline(x=mean,color='red',label='mean')
    plt.axvline(x=median,color='blue',label='median')
    plt.axvline(x=mode,color='yellow',label='mode')
    plt.legend()
    plt.show()


