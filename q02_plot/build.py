# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    Mean = sale_price.mean()
    Median = sale_price.median()
    Mode = sale_price.mode().iloc[0]
    plt.hist(sale_price, bins=30)    
    plt.axvline(Mean, color='r')
    plt.axvline(Median, color='b')
    plt.axvline(Mode, color='g')
    plt.show()



