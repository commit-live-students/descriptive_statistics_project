# %load q02_plot/build.py
# Default Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    
    Mean = sale_price.mean()
    Median = np.median(sale_price)
    Mode = sale_price.mode()
    
    plt.hist(sale_price, bins=40)
    plt.axvline(Mean, color='red')
    plt.axvline(Median, color='green')
    plt.axvline(Mode[0], color='black')
    plt.xlabel('Sale Price')
    plt.ylabel('Frequency')
    plt.show()



