# %load q02_plot/build.py
# Default Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

#To be uncommented while test case check
#plt.switch_backend('agg')



# Draw the plot for the mean, median and mode for the dataset
def plot():

    dataframe = pd.read_csv('data/house_prices_multivariate.csv')
    sale_price = dataframe.loc[:, 'SalePrice']

    plt.hist(sale_price, bins=60)

    plt.axvline(x=sale_price.mean(),color='red',linestyle='--',label='Mean')
    plt.axvline(x=sale_price.median(),color='black',linestyle='--',label='Median')
    plt.axvline(x=sale_price.mode()[0],color='orange',linestyle='--',label='Mode')

    plt.legend(loc=0)

    plt.show()
    
plot()





